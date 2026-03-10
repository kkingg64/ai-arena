# 🀄 P2026-004 AI Arena - Mahjong Game Logic

## 📁 Project Structure

```
app/
├── components/
│   ├── MahjongTile.tsx      # 3D Tile Component
│   ├── MahjongTable.tsx     # Main Table Scene + Animations
│   └── MahjongTile.js       # Pure Three.js version
├── hooks/
│   └── useMahjongGame.ts    # Game Logic Hook
├── utils/
│   └── MahjongTileMap.ts    # 144 Tiles → Asset Paths
└── public/
    └── assets/
        └── tiles/           # Tile images (144)
```

## 🎮 useMahjongGame Hook

### Game State

```typescript
interface MahjongGameState {
  phase: 'idle' | 'dealing' | 'drawing' | 'discarding' | 'claiming' | 'scoring';
  currentPlayer: number;     // 0-3
  dealer: number;            // 0-3
  round: number;             // 1-4 (東南西北)
  subRound: number;          // 局數
  basePoints: number;        // 本場
  wall: TileDefinition[];    // 144 tiles
  hands: TileDefinition[][]; // 4 players' hands
  discards: TileDefinition[][]; // 4 players' discards
  scores: number[];          // 4 players' scores
  actionCandidates: ActionCandidate[]; // Pong/Kong/Hu
  selectedTile: { player: number; index: number } | null;
}
```

### Core Functions

| Function | Description |
|----------|-------------|
| `initializeGame()` | 洗牌 + 發牌 (每人13張) |
| `drawTile(playerIndex)` | 摸牌 |
| `discardTile(playerIndex, tileIndex)` | 打牌 |
| `selectTile(playerIndex, tileIndex)` | 選牌 |
| `confirmDiscard()` | 確認打牌 |
| `claimAction(candidate)` | 碰/槓/食糊 |
| `skipAction()` | 過 |

### Action Candidates (廣東話)

- **碰** - Pong
- **槓** - Kong  
- **食糊** - Hu (Win)

## 🎬 Animations

### Technology
- **framer-motion-3d** - Spring physics animations
- **React Three Fiber** - 3D rendering

### AnimatedTile Component
- Uses spring physics (stiffness: 300, damping: 25)
- Selection: 牌向上位移 0.08 units
- Card dealing: staggered delay per tile

### Camera Effects (Placeholder)
- Camera shake on discard (placeholder)
- Sound effects (placeholder)

## 🀄 MahjongTable.tsx Features

### 1. 中央記分板 (Central Hub)
- Frosted glass effect
- Round info (東 2 局)
- Dealer info (莊家：東)
- 4 player scores with billboard effect

### 2. 棄牌區 (Discard River)
- 6x3 grid per player
- Rotated based on player position
- 0.01 gap to prevent Z-fighting

### 3. 手牌 (Player Hand)
- 14 tiles with 15° tilt
- Spring animation on selection
- Only player 0 shows face-up

### 4. Action Buttons (廣東話)
- 碰 / 槓 / 食糊 / 過
- Appears when action available

### 5. 燈光
- Ambient + Spot + Point lights
- Environment preset: night
- Contact shadows

## 🚀 Usage

```tsx
import { MahjongTable } from './components/MahjongTable';

function App() {
  return (
    <Canvas>
      <MahjongTable 
        onGameAction={(action) => console.log(action)}
      />
    </Canvas>
  );
}
```

## 📋 Next Steps

1. ✅ MahjongTile component
2. ✅ MahjongTable component
3. ✅ useMahjongGame hook
4. ⏳ Connect to rlcard engine (Phase 3)
5. ⏳ Add AI integration
6. ⏳ Web deployment

---

*Phase 2 - Game Logic Confirmed*
*Last Updated: 2026-03-09*
