/**
 * MahjongTable.tsx - Updated with Animations
 * 
 * Main 3D Mahjong Table Scene with Game Logic
 */

import React, { useRef, useMemo, useEffect, useState } from 'react';
import { ThreeEvent } from '@react-three/fiber';
import { Text, Html, Environment, ContactShadows } from '@react-three/drei';
import { motion } from 'framer-motion-3d';
import * as THREE from 'three';
import { MahjongTile } from './MahjongTile';
import { useMahjongGame, ActionCandidate } from '../hooks/useMahjongGame';

// Table constants
const TABLE_SIZE = 8;
const TILE_WIDTH = 0.3;
const TILE_HEIGHT = 0.4;
const TILE_DEPTH = 0.2;
const TILE_GAP = 0.01;

// Player positions (南=0, 西=1, 北=2, 東=3 in HK style)
const PLAYER_POSITIONS = [
  { position: [0, 0, 2.8], rotation: [0, 0, 0], label: '南', direction: 'South' },
  { position: [2.8, 0, 0], rotation: [0, Math.PI / 2, 0], label: '西', direction: 'West' },
  { position: [0, 0, -2.8], rotation: [0, Math.PI, 0], label: '北', direction: 'North' },
  { position: [-2.8, 0, 0], rotation: [0, -Math.PI / 2, 0], label: '東', direction: 'East' },
];

// Discard grid: 6 columns x 3 rows
const DISCARD_ROWS = 3;
const DISCARD_COLS = 6;

// Calculate discard position
function getDiscardPosition(
  playerIndex: number, 
  tileIndex: number
): { position: [number, number, number]; rotation: [number, number, number] } {
  const row = Math.floor(tileIndex / DISCARD_COLS);
  const col = tileIndex % DISCARD_COLS;
  
  const distanceFromCenter = 1.3;
  const tileSpacingX = TILE_WIDTH + TILE_GAP;
  const tileSpacingZ = TILE_HEIGHT + TILE_GAP;
  
  let x = 0, z = 0, rotY = 0;
  
  switch (playerIndex) {
    case 0: // South (Bottom)
      x = (col - DISCARD_COLS / 2 + 0.5) * tileSpacingX;
      z = distanceFromCenter + row * tileSpacingZ;
      rotY = 0;
      break;
    case 1: // West (Right)
      z = (col - DISCARD_COLS / 2 + 0.5) * tileSpacingX;
      x = -(distanceFromCenter + row * tileSpacingZ);
      rotY = Math.PI / 2;
      break;
    case 2: // North (Top)
      x = -(col - DISCARD_COLS / 2 + 0.5) * tileSpacingX;
      z = -(distanceFromCenter + row * tileSpacingZ);
      rotY = Math.PI;
      break;
    case 3: // East (Left)
      z = -(col - DISCARD_COLS / 2 + 0.5) * tileSpacingX;
      x = distanceFromCenter + row * tileSpacingZ;
      rotY = -Math.PI / 2;
      break;
  }
  
  return {
    position: [x, 0.1, z],
    rotation: [0, rotY, 0],
  };
}

// Calculate hand position with 15-degree tilt
function getHandPosition(
  playerIndex: number,
  tileIndex: number,
  isDrawnTile: boolean = false
): { position: [number, number, number]; rotation: [number, number, number] } {
  const tileSpacing = TILE_WIDTH + 0.003;
  const handSize = 14;
  const handOffset = (handSize - 1) * tileSpacing / 2;
  
  const distances = [3.0, 3.0, 3.0, 3.0];
  const distance = distances[playerIndex];
  
  let x = 0, z = 0, rotY = 0, tiltX = -0.26; // ~15 degrees
  
  switch (playerIndex) {
    case 0: // South
      x = tileIndex * tileSpacing - handOffset;
      z = distance;
      rotY = 0;
      break;
    case 1: // West
      z = tileIndex * tileSpacing - handOffset;
      x = -distance;
      rotY = Math.PI / 2;
      break;
    case 2: // North
      x = -(tileIndex * tileSpacing - handOffset);
      z = -distance;
      rotY = Math.PI;
      break;
    case 3: // East
      z = -(tileIndex * tileSpacing - handOffset);
      x = distance;
      rotY = -Math.PI / 2;
      break;
  }
  
  return {
    position: [x, 0, z],
    rotation: [tiltX, rotY, 0],
  };
}

// Animated Tile Component
interface AnimatedTileProps {
  suit: string;
  value: string;
  position: [number, number, number];
  rotation: [number, number, number];
  isFaceDown?: boolean;
  isSelected?: boolean;
  isInteractive?: boolean;
  onClick?: (e: ThreeEvent<MouseEvent>) => void;
  delay?: number;
}

const AnimatedTile: React.FC<AnimatedTileProps> = ({
  suit,
  value,
  position,
  rotation,
  isFaceDown = false,
  isSelected = false,
  isInteractive = true,
  onClick,
  delay = 0,
}) => {
  const selectedOffset = isSelected ? -0.08 : 0;
  
  return (
    <motion.group
      animate={{
        position: [position[0], position[1] + selectedOffset, position[2]],
      }}
      transition={{
        type: "spring",
        stiffness: 300,
        damping: 25,
        delay: delay,
      }}
    >
      <MahjongTile
        suit={suit}
        value={value}
        position={position}
        rotation={rotation}
        isFaceDown={isFaceDown}
        isSelected={isSelected}
        isInteractive={isInteractive}
        onClick={onClick}
      />
    </motion.group>
  );
};

interface MahjongTableProps {
  onGameAction?: (action: ActionCandidate) => void;
}

export const MahjongTable: React.FC<MahjongTableProps> = ({
  onGameAction,
}) => {
  const {
    state,
    initializeGame,
    drawTile,
    discardTile,
    selectTile,
    confirmDiscard,
    claimAction,
    skipAction,
  } = useMahjongGame(onGameAction);

  const [showActionButtons, setShowActionButtons] = useState(false);

  // Start game on mount
  useEffect(() => {
    initializeGame();
  }, [initializeGame]);

  // Show action buttons when candidates exist
  useEffect(() => {
    setShowActionButtons(state.actionCandidates.length > 0 && state.phase === 'claiming');
  }, [state.actionCandidates, state.phase]);

  // Handle tile click
  const handleTileClick = (playerIndex: number, tileIndex: number) => {
    if (state.phase !== 'discarding') return;
    if (playerIndex !== state.currentPlayer) return;
    
    // Select tile
    selectTile(playerIndex, tileIndex);
  };

  // Handle discard confirmation
  const handleDiscard = () => {
    if (state.selectedTile) {
      discardTile(state.selectedTile.player, state.selectedTile.index);
    }
  };

  // Camera shake on discard (placeholder)
  const handleCameraShake = () => {
    // Placeholder for camera shake effect
    console.log("Camera shake triggered");
  };

  // Get round string
  const getRoundString = () => {
    const directions = ['東', '南', '西', '北'];
    return `${directions[state.round - 1]} ${state.subRound} 局`;
  };

  // Get dealer direction
  const getDealerString = () => {
    const directions = ['南', '西', '北', '東'];
    return directions[state.dealer];
  };

  return (
    <group>
      {/* Lighting */}
      <ambientLight intensity={0.5} />
      <spotLight
        position={[0, 12, 0]}
        angle={0.6}
        penumbra={0.5}
        intensity={1.5}
        castShadow
        shadow-mapSize={[2048, 2048]}
      />
      <pointLight position={[5, 5, 5]} intensity={0.3} color="#4488ff" />
      <pointLight position={[-5, 5, -5]} intensity={0.3} color="#ff8844" />
      
      <Environment preset="night" />

      {/* Table Surface */}
      <mesh 
        rotation={[-Math.PI / 2, 0, 0]} 
        position={[0, -0.06, 0]} 
        receiveShadow
      >
        <planeGeometry args={[TABLE_SIZE, TABLE_SIZE]} />
        <meshStandardMaterial 
          color="#0d1b2a"
          roughness={0.75}
          metalness={0.05}
        />
      </mesh>

      {/* Central Hub - Frosted Glass */}
      <group position={[0, 0.03, 0]}>
        {/* Main glass panel */}
        <mesh rotation={[-Math.PI / 2, 0, 0]}>
          <cylinderGeometry args={[1.3, 1.3, 0.06, 32]} />
          <meshPhysicalMaterial
            color="#ffffff"
            transmission={0.85}
            thickness={0.5}
            roughness={0.05}
            clearcoat={1}
            transparent
            opacity={0.25}
          />
        </mesh>
        
        {/* Round Info */}
        <Text
          position={[0, 0.04, 0]}
          rotation={[-Math.PI / 2, 0, 0]}
          fontSize={0.35}
          color="#ffd700"
          anchorX="center"
          anchorY="middle"
        >
          {getRoundString()}
        </Text>
        
        {/* Dealer */}
        <Text
          position={[0, 0.04, -0.45]}
          rotation={[-Math.PI / 2, 0, 0]}
          fontSize={0.14}
          color="#888888"
          anchorX="center"
        >
          莊家：{getDealerString()}
        </Text>

        {/* Player Scores */}
        {state.scores.map((score, index) => {
          const angle = (index * Math.PI) / 2;
          const radius = 1.05;
          const x = Math.sin(angle) * radius;
          const z = Math.cos(angle) * radius;
          
          return (
            <group key={index} position={[x, 0.04, z]}>
              <Text
                rotation={[-Math.PI / 2, 0, 0]}
                fontSize={0.2}
                color={index === state.currentPlayer ? "#00d4ff" : "#ffffff"}
                anchorX="center"
                anchorY="middle"
              >
                {score.toLocaleString()}
              </Text>
              <Text
                position={[0, 0, 0.18]}
                rotation={[-Math.PI / 2, 0, 0]}
                fontSize={0.1}
                color="#666666"
                anchorX="center"
              >
                {PLAYER_POSITIONS[index].label}
              </Text>
            </group>
          );
        })}
      </group>

      {/* Discard Tiles with Animation */}
      {state.discards.map((playerDiscards, playerIndex) => (
        <group key={`discards-${playerIndex}`}>
          {playerDiscards.map((tile, tileIndex) => {
            const { position, rotation } = getDiscardPosition(playerIndex, tileIndex);
            return (
              <AnimatedTile
                key={`d-${playerIndex}-${tileIndex}`}
                suit={tile.suit}
                value={tile.value}
                position={position}
                rotation={rotation}
                isFaceDown={true}
                isInteractive={false}
                delay={tileIndex * 0.05}
              />
            );
          })}
        </group>
      ))}

      {/* Player Hands with Animation */}
      {state.hands.map((hand, playerIndex) => (
        <group key={`hand-${playerIndex}`}>
          {hand.map((tile, tileIndex) => {
            const { position, rotation } = getHandPosition(playerIndex, tileIndex, tileIndex === 13);
            const isCurrentPlayer = playerIndex === state.currentPlayer;
            const isSelected = state.selectedTile?.player === playerIndex && 
                             state.selectedTile?.index === tileIndex;
            
            return (
              <AnimatedTile
                key={`h-${playerIndex}-${tileIndex}`}
                suit={tile.suit}
                value={tile.value}
                position={position}
                rotation={rotation}
                isFaceDown={playerIndex !== 0}
                isSelected={isSelected}
                isInteractive={isCurrentPlayer && state.phase === 'discarding'}
                onClick={(e) => {
                  e.stopPropagation();
                  handleTileClick(playerIndex, tileIndex);
                }}
                delay={tileIndex * 0.02}
              />
            );
          })}
        </group>
      ))}

      {/* Player Labels */}
      {PLAYER_POSITIONS.map((player, index) => (
        <group 
          key={`label-${index}`} 
          position={player.position}
          rotation={player.rotation}
        >
          <Html
            position={[0, 1.2, 0]}
            center
            style={{
              background: 'rgba(0,0,0,0.6)',
              backdropFilter: 'blur(10px)',
              padding: '8px 14px',
              borderRadius: '12px',
              border: `2px solid ${index === state.currentPlayer ? '#00d4ff' : 'rgba(255,255,255,0.2)'}`,
              whiteSpace: 'nowrap',
              transition: 'all 0.3s ease',
            }}
          >
            <div style={{ 
              color: index === state.currentPlayer ? '#00d4ff' : '#fff', 
              fontWeight: 'bold',
              fontSize: '14px',
            }}>
              {['GPT-4o', 'Claude', 'Gemini', 'Llama'][index]}
            </div>
            <div style={{ color: '#888', fontSize: '11px' }}>
              {player.label}
            </div>
          </Html>
        </group>
      ))}

      {/* Action Buttons (Pong/Kong/Hu) */}
      {showActionButtons && (
        <Html center position={[0, 2, 0]}>
          <div style={{
            display: 'flex',
            gap: '10px',
            background: 'rgba(0,0,0,0.8)',
            backdropFilter: 'blur(10px)',
            padding: '12px 20px',
            borderRadius: '16px',
            border: '1px solid rgba(255,255,255,0.2)',
          }}>
            {state.actionCandidates.map((candidate, idx) => (
              <button
                key={idx}
                onClick={() => claimAction(candidate)}
                style={{
                  background: candidate.type === 'hu' ? '#ffd700' : '#00d4ff',
                  color: candidate.type === 'hu' ? '#000' : '#000',
                  border: 'none',
                  padding: '10px 20px',
                  borderRadius: '10px',
                  fontWeight: 'bold',
                  fontSize: '14px',
                  cursor: 'pointer',
                  transition: 'transform 0.2s',
                }}
              >
                {candidate.type === 'pong' && '碰'}
                {candidate.type === 'kong' && '槓'}
                {candidate.type === 'hu' && '食糊'}
              </button>
            ))}
            <button
              onClick={skipAction}
              style={{
                background: 'rgba(255,255,255,0.2)',
                color: '#fff',
                border: '1px solid rgba(255,255,255,0.3)',
                padding: '10px 20px',
                borderRadius: '10px',
                fontWeight: 'bold',
                fontSize: '14px',
                cursor: 'pointer',
              }}
            >
              過
            </button>
          </div>
        </Html>
      )}

      {/* Discard Button (when tile selected) */}
      {state.selectedTile && state.phase === 'discarding' && (
        <Html center position={[0, -2.5, 0]}>
          <button
            onClick={() => {
              handleDiscard();
              handleCameraShake();
            }}
            style={{
              background: '#ff4444',
              color: '#fff',
              border: 'none',
              padding: '14px 40px',
              borderRadius: '12px',
              fontWeight: 'bold',
              fontSize: '16px',
              cursor: 'pointer',
              boxShadow: '0 4px 20px rgba(255,68,68,0.4)',
            }}
          >
            🀄 打出呢隻牌
          </button>
        </Html>
      )}

      {/* Phase indicator */}
      <Html center position={[0, 3.5, 0]}>
        <div style={{
          color: '#666',
          fontSize: '12px',
          background: 'rgba(0,0,0,0.5)',
          padding: '4px 12px',
          borderRadius: '20px',
        }}>
          Phase: {state.phase} | 牌牆: {state.wall.length} 張
        </div>
      </Html>

      {/* Contact shadows */}
      <ContactShadows
        position={[0, -0.05, 0]}
        opacity={0.4}
        scale={TABLE_SIZE}
        blur={2.5}
        far={8}
      />
    </group>
  );
};

export default MahjongTable;
