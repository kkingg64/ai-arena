/**
 * MahjongTileMap.ts
 * 
 * Maps 144 tile IDs to asset paths
 * Hong Kong Mahjong - 144 tiles total
 */

// Tile ID structure: {suit}_{value}_{index}
// Example: "萬_1_0" = 萬子 1st copy

export interface TileDefinition {
  id: string;
  suit: string;
  value: string;
  suitEn: string;
  valueEn: string;
  assetPath: string;
}

// Hong Kong Mahjong suits
export const SUITS = {
  CHARACTERS: '萬',  // Characters (万子)
  DOTS: '筒',       // Dots (筒子)
  BAMBOO: '索',     // Bamboo (索子)
  WINDS: '番子',    // Winds (東南西北)
  HONORS: '字',     // Honors (中發白)
};

// Map Chinese suit to English folder name
export const SUIT_TO_FOLDER: Record<string, string> = {
  '萬': 'characters',
  '筒': 'dots',
  '索': 'bamboo',
  '番子': 'winds',
  '字': 'honors',
};

// Map Chinese value to English filename
export const VALUE_TO_FILENAME: Record<string, string> = {
  // Numbers
  '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
  '6': '6', '7': '7', '8': '8', '9': '9',
  // Winds
  '東': 'east', '南': 'south', '西': 'west', '北': 'north',
  // Honors
  '中': 'red', '發': 'green', '白': 'white',
};

/**
 * Generate asset path for a tile
 */
export function getTileAssetPath(suit: string, value: string): string {
  const folder = SUIT_TO_FOLDER[suit] || 'characters';
  const filename = VALUE_TO_FILENAME[value] || value;
  return `/assets/tiles/${folder}_${filename}.png`;
}

/**
 * Generate all 144 tile definitions for Hong Kong Mahjong
 */
export function generateMahjongTiles(): TileDefinition[] {
  const tiles: TileDefinition[] = [];
  
  // Numbers 1-9 for each suit (4 copies each = 108 tiles)
  const numberValues = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
  const suits = [SUITS.CHARACTERS, SUITS.DOTS, SUITS.BAMBOO];
  
  suits.forEach(suit => {
    numberValues.forEach(value => {
      for (let i = 0; i < 4; i++) {
        tiles.push({
          id: `${suit}_${value}_${i}`,
          suit,
          value,
          suitEn: SUIT_TO_FOLDER[suit],
          valueEn: VALUE_TO_FILENAME[value],
          assetPath: getTileAssetPath(suit, value),
        });
      }
    });
  });
  
  // Winds (4 each = 16 tiles)
  const windValues = ['東', '南', '西', '北'];
  windValues.forEach(value => {
    for (let i = 0; i < 4; i++) {
      tiles.push({
        id: `番子_${value}_${i}`,
        suit: SUITS.WINDS,
        value,
        suitEn: 'winds',
        valueEn: VALUE_TO_FILENAME[value],
        assetPath: getTileAssetPath(SUITS.WINDS, value),
      });
    }
  });
  
  // Honors (4 each = 12 tiles)
  const honorValues = ['中', '發', '白'];
  honorValues.forEach(value => {
    for (let i = 0; i < 4; i++) {
      tiles.push({
        id: `字_${value}_${i}`,
        suit: SUITS.HONORS,
        value,
        suitEn: 'honors',
        valueEn: VALUE_TO_FILENAME[value],
        assetPath: getTileAssetPath(SUITS.HONORS, value),
      });
    }
  });
  
  // Flowers (1 each = 8 tiles)
  const flowerValues = ['春', '夏', '秋', '冬', '梅', '蘭', '菊', '竹'];
  flowerValues.forEach((value, index) => {
    tiles.push({
      id: `花_${value}_0`,
      suit: '花',
      value,
      suitEn: 'flowers',
      valueEn: String(index + 1),
      assetPath: `/assets/tiles/flowers_${value}.png`,
    });
  });
  
  return tiles;
}

/**
 * Get tile by ID
 */
export function getTileById(id: string): TileDefinition | undefined {
  const tiles = generateMahjongTiles();
  return tiles.find(t => t.id === id);
}

/**
 * Generate a random hand of 13/14 tiles
 */
export function generateRandomHand(count: number = 13): TileDefinition[] {
  const allTiles = generateMahjongTiles();
  const shuffled = [...allTiles].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, count);
}

// Export all tile definitions
export const HONG_KONG_MAHJONG_TILES = generateMahjongTiles();

export default {
  SUITS,
  SUIT_TO_FOLDER,
  VALUE_TO_FILENAME,
  getTileAssetPath,
  generateMahjongTiles,
  getTileById,
  generateRandomHand,
  HONG_KONG_MAHJONG_TILES,
};
