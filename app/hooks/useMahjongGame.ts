/**
 * useMahjongGame.ts
 * 
 * Hong Kong Mahjong Game Logic Hook
 * 
 * @param onAction - Callback for game actions (Pong, Kong, Hu)
 */

import { useState, useCallback, useEffect, useRef } from 'react';
import { 
  generateMahjongTiles, 
  TileDefinition,
  getTileAssetPath 
} from '../utils/MahjongTileMap';

// Game phases
export type GamePhase = 'idle' | 'dealing' | 'drawing' | 'discarding' | 'claiming' | 'scoring';

// Player action types
export type PlayerAction = 'draw' | 'discard' | 'pong' | 'kong' | 'hu';

// Action candidate for Pon/Kong/Hu
export interface ActionCandidate {
  type: 'pong' | 'kong' | 'hu';
  playerIndex: number;
  tiles: TileDefinition[];
}

// Game state interface
export interface MahjongGameState {
  phase: GamePhase;
  currentPlayer: number;
  dealer: number;
  round: number;      // 1-4 (東西南北)
  subRound: number;   // 1-? (局數)
  basePoints: number; // 本場 points
  wall: TileDefinition[];
  hands: TileDefinition[][];
  discards: TileDefinition[][];
  scores: number[];
  lastAction: {
    player: number;
    action: PlayerAction;
    tile?: TileDefinition;
  } | null;
  actionCandidates: ActionCandidate[];
  selectedTile: { player: number; index: number } | null;
}

const INITIAL_SCORE = 25000;
const HAND_SIZE = 13;
const TILES_PER_DRAW = 4;

export function useMahjongGame(onAction?: (action: ActionCandidate) => void) {
  const [state, setState] = useState<MahjongGameState>({
    phase: 'idle',
    currentPlayer: 0,
    dealer: 0,
    round: 1,       // 東
    subRound: 1,   // 東一局
    basePoints: 0, // 本場
    wall: [],
    hands: [[], [], [], []],
    discards: [[], [], [], []],
    scores: [INITIAL_SCORE, INITIAL_SCORE, INITIAL_SCORE, INITIAL_SCORE],
    lastAction: null,
    actionCandidates: [],
    selectedTile: null,
  });

  const animationRef = useRef<{
    isAnimating: boolean;
    animationType: string | null;
  }>({ isAnimating: false, animationType: null });

  // Initialize and shuffle wall
  const initializeGame = useCallback(() => {
    const tiles = generateMahjongTiles();
    
    // Fisher-Yates shuffle
    for (let i = tiles.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [tiles[i], tiles[j]] = [tiles[j], tiles[i]];
    }

    // Deal 13 tiles to each player
    const hands: TileDefinition[][] = [[], [], [], []];
    for (let i = 0; i < HAND_SIZE; i++) {
      for (let p = 0; p < 4; p++) {
        hands[p].push(tiles.pop()!);
      }
    }

    setState(prev => ({
      ...prev,
      phase: 'dealing',
      wall: tiles,
      hands,
      discards: [[], [], [], []],
      currentPlayer: prev.dealer,
      lastAction: null,
      actionCandidates: [],
      selectedTile: null,
    }));

    animationRef.current = { isAnimating: true, animationType: 'dealing' };

    // After dealing animation, start first draw
    setTimeout(() => {
      setState(prev => ({
        ...prev,
        phase: 'drawing',
      }));
      animationRef.current = { isAnimating: false, animationType: null };
    }, 2000);
  }, []);

  // Draw a tile from wall
  const drawTile = useCallback((playerIndex: number) => {
    setState(prev => {
      if (prev.wall.length === 0) {
        // No more tiles - draw game
        return { ...prev, phase: 'scoring' };
      }

      const newWall = [...prev.wall];
      const drawnTile = newWall.pop()!;
      const newHands = prev.hands.map((hand, i) => 
        i === playerIndex ? [...hand, drawnTile] : [...hand]
      );

      // Sort hand
      newHands[playerIndex].sort((a, b) => {
        const suitOrder = ['萬', '筒', '索', '番子', '字', '花'];
        const aSuit = suitOrder.indexOf(a.suit);
        const bSuit = suitOrder.indexOf(b.suit);
        if (aSuit !== bSuit) return aSuit - bSuit;
        return parseInt(a.value) - parseInt(b.value);
      });

      return {
        ...prev,
        phase: 'discarding',
        wall: newWall,
        hands: newHands,
        lastAction: {
          player: playerIndex,
          action: 'draw',
          tile: drawnTile,
        },
      };
    });

    // Check for winning hand (食糊)
    checkForHu(state.currentPlayer);
  }, [state.currentPlayer]);

  // Discard a tile
  const discardTile = useCallback((playerIndex: number, tileIndex: number) => {
    setState(prev => {
      const newHands = prev.hands.map((hand, i) => 
        i === playerIndex ? hand.filter((_, idx) => idx !== tileIndex) : [...hand]
      );
      
      const discardedTile = prev.hands[playerIndex][tileIndex];
      
      const newDiscards = prev.discards.map((pile, i) => 
        i === playerIndex ? [...pile, discardedTile] : [...pile]
      );

      // Check for next player
      const nextPlayer = (playerIndex + 1) % 4;

      // Check for action candidates (Pong/Kong/Hu)
      const candidates = checkForActions(nextPlayer, discardedTile);

      if (candidates.length > 0 && onAction) {
        onAction(candidates[0]);
      }

      return {
        ...prev,
        phase: candidates.length > 0 ? 'claiming' : 'drawing',
        hands: newHands,
        discards: newDiscards,
        currentPlayer: nextPlayer,
        lastAction: {
          player: playerIndex,
          action: 'discard',
          tile: discardedTile,
        },
        actionCandidates: candidates,
        selectedTile: null,
      };
    });
  }, [onAction]);

  // Check for Hu (食糊)
  const checkForHu = (playerIndex: number) => {
    const hand = state.hands[playerIndex];
    if (!hand || hand.length !== 14) return;

    // Simplified win detection (check for 4 sets + 1 pair)
    // In real implementation, use rlcard or proper Mahjong logic
    const isWinningHand = detectWin(hand);
    
    if (isWinningHand) {
      const candidate: ActionCandidate = {
        type: 'hu',
        playerIndex,
        tiles: [hand[hand.length - 1]],
      };
      
      setState(prev => ({
        ...prev,
        actionCandidates: [...prev.actionCandidates, candidate],
      }));

      if (onAction) onAction(candidate);
    }
  };

  // Simple win detection (simplified)
  const detectWin = (hand: TileDefinition[]): boolean => {
    // This is a placeholder - real implementation needs rlcard
    // For demo, randomly suggest Hu sometimes
    return Math.random() < 0.05;
  };

  // Check for Pong/Kong
  const checkForActions = (playerIndex: number, tile: TileDefinition): ActionCandidate[] => {
    const candidates: ActionCandidate[] = [];
    const hand = state.hands[playerIndex];
    
    if (!hand) return candidates;

    // Check for Pong (2 same tiles)
    const sameTiles = hand.filter(t => t.suit === tile.suit && t.value === tile.value);
    if (sameTiles.length >= 2) {
      candidates.push({
        type: 'pong',
        playerIndex,
        tiles: [tile, ...sameTiles.slice(0, 2)],
      });
    }

    // Check for Kong (3 same tiles + 1)
    if (sameTiles.length >= 3) {
      candidates.push({
        type: 'kong',
        playerIndex,
        tiles: [tile, ...sameTiles.slice(0, 3)],
      });
    }

    // Check for Hu (simplified)
    if (hand.length === 13) {
      // Check if adding this tile makes a winning hand
      const testHand = [...hand, tile];
      if (detectWin(testHand)) {
        candidates.push({
          type: 'hu',
          playerIndex,
          tiles: [tile],
        });
      }
    }

    return candidates;
  };

  // Player claims action (Pong/Kong)
  const claimAction = useCallback((candidate: ActionCandidate) => {
    if (candidate.type === 'hu') {
      // Player wins!
      handleWin(candidate.playerIndex, candidate.tiles[0]);
      return;
    }

    // Handle Pong/Kong
    setState(prev => {
      const newHand = [...prev.hands[candidate.playerIndex]];
      
      // Add the claimed tile
      if (prev.lastAction?.tile) {
        newHand.push(prev.lastAction.tile);
      }

      // Add tiles to meld
      candidate.tiles.forEach(t => {
        const idx = newHand.findIndex(h => h.suit === t.suit && h.value === t.value);
        if (idx > -1) newHand.splice(idx, 1);
      });

      const newHands = prev.hands.map((h, i) => 
        i === candidate.playerIndex ? newHand : h
      );

      return {
        ...prev,
        phase: 'discarding',
        hands: newHands,
        currentPlayer: candidate.playerIndex,
        actionCandidates: [],
        selectedTile: null,
      };
    });
  }, []);

  // Skip action
  const skipAction = useCallback(() => {
    setState(prev => ({
      ...prev,
      phase: 'drawing',
      actionCandidates: [],
    }));
  }, []);

  // Handle win
  const handleWin = (winner: number, winningTile: TileDefinition) => {
    // Calculate points and update scores
    setState(prev => {
      const newScores = [...prev.scores];
      const winPoints = 1000; // Simplified
      
      // Deduct from other players
      for (let i = 0; i < 4; i++) {
        if (i !== winner) {
          newScores[i] -= winPoints;
        }
      }
      // Add to winner
      newScores[winner] += winPoints * 3;

      return {
        ...prev,
        phase: 'scoring',
        scores: newScores,
      };
    });
  };

  // Select a tile
  const selectTile = useCallback((playerIndex: number, tileIndex: number) => {
    if (state.phase !== 'discarding' || state.currentPlayer !== playerIndex) return;

    setState(prev => ({
      ...prev,
      selectedTile: { player: playerIndex, index: tileIndex },
    }));
  }, [state.phase, state.currentPlayer]);

  // Confirm discard
  const confirmDiscard = useCallback(() => {
    if (!state.selectedTile) return;
    discardTile(state.selectedTile.player, state.selectedTile.index);
  }, [state.selectedTile, discardTile]);

  // Get animation state
  const getAnimationState = useCallback(() => {
    return animationRef.current;
  }, []);

  return {
    state,
    initializeGame,
    drawTile,
    discardTile,
    selectTile,
    confirmDiscard,
    claimAction,
    skipAction,
    getAnimationState,
  };
}

export default useMahjongGame;
