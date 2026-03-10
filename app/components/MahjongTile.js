/**
 * MahjongTile.js
 * 
 * Pure Three.js 3D Mahjong Tile Component
 * Proportions: 3:4:2 (width:height:depth)
 * 
 * Usage:
 *   const tile = createMahjongTile(scene, '萬', '1', { x: 0, y: 0, z: 0 });
 */

import * as THREE from 'three';

// Tile dimensions (3:4:2 ratio)
const TILE_WIDTH = 0.3;
const TILE_HEIGHT = 0.4;
const TILE_DEPTH = 0.2;

// Suit mapping to folder names
const SUIT_MAP = {
  '萬': 'characters',
  '筒': 'dots',
  '索': 'bamboo',
  '番子': 'winds',
  '字': 'honors',
};

// Value mapping for image filenames
const VALUE_MAP = {
  '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
  '6': '6', '7': '7', '8': '8', '9': '9',
  '東': 'east', '南': 'south', '西': 'west', '北': 'north',
  '中': 'red', '發': 'green', '白': 'white',
};

/**
 * Create a 3D Mahjong Tile
 * @param {THREE.Scene} scene - Three.js scene
 * @param {string} suit - 萬/筒/索/番子
 * @param {string} value - 1-9 or 東/南/西/北/中/發/白
 * @param {Object} options - { x, y, z, isFaceDown, onClick }
 * @returns {THREE.Group} - The tile group
 */
export function createMahjongTile(scene, suit, value, options = {}) {
  const {
    x = 0,
    y = 0,
    z = 0,
    isFaceDown = false,
    onClick = null,
  } = options;

  // Create group
  const tileGroup = new THREE.Group();
  tileGroup.position.set(x, y, z);

  // Create geometry (3:4:2 ratio box)
  const geometry = new THREE.BoxGeometry(TILE_WIDTH, TILE_HEIGHT, TILE_DEPTH);

  // Create materials for each face
  // BoxGeometry faces: +X, -X, +Y, -Y, +Z, -Z
  
  // Ivory material for sides
  const ivoryMaterial = new THREE.MeshStandardMaterial({
    color: 0xf8f4eb,
    roughness: 0.4,
    metalness: 0.05,
  });

  // Front face material (shows to player)
  let frontMaterial;
  if (isFaceDown) {
    // Deep blue back
    frontMaterial = new THREE.MeshStandardMaterial({
      color: 0x1a3a5c,
      roughness: 0.3,
      metalness: 0.1,
    });
  } else {
    // Ivory front with texture
    frontMaterial = new THREE.MeshStandardMaterial({
      color: 0xf8f4eb,
      roughness: 0.4,
      metalness: 0.05,
    });
  }

  // Back material (ivory)
  const backMaterial = new THREE.MeshStandardMaterial({
    color: 0xf8f4eb,
    roughness: 0.4,
    metalness: 0.05,
  });

  // Apply materials: [right, left, top, bottom, front, back]
  const materials = [
    ivoryMaterial,   // +X (right)
    ivoryMaterial,  // -X (left)
    ivoryMaterial,  // +Y (top)
    ivoryMaterial,  // -Y (bottom)
    frontMaterial,  // +Z (front)
    backMaterial,   // -Z (back)
  ];

  // Create mesh
  const tileMesh = new THREE.Mesh(geometry, materials);
  tileMesh.castShadow = true;
  tileMesh.receiveShadow = true;
  
  // Add user data for click handling
  tileMesh.userData = {
    type: 'mahjongTile',
    suit,
    value,
    isFaceDown,
  };

  tileGroup.add(tileMesh);

  // Add edge lines for better visibility
  const edges = new THREE.EdgesGeometry(geometry);
  const lineMaterial = new THREE.LineBasicMaterial({ 
    color: 0x000000, 
    opacity: 0.2, 
    transparent: true 
  });
  const wireframe = new THREE.LineSegments(edges, lineMaterial);
  tileGroup.add(wireframe);

  // Add to scene
  if (scene) {
    scene.add(tileGroup);
  }

  // Add click handler if provided
  if (onClick && scene) {
    // Setup raycaster for click detection
    // This would be handled by the main game loop
    tileGroup.userData.onClick = onClick;
  }

  return tileGroup;
}

/**
 * Generate texture path for tile
 * @param {string} suit 
 * @param {string} value 
 * @returns {string} texture path
 */
export function getTileTexturePath(suit, value) {
  const suitFolder = SUIT_MAP[suit] || 'characters';
  const valueStr = VALUE_MAP[value] || value;
  return `/assets/tiles/${suitFolder}_${valueStr}.png`;
}

/**
 * Create all 144 Hong Kong Mahjong tiles
 * @param {THREE.Scene} scene 
 * @returns {Map} tile map
 */
export function createMahjongSet(scene) {
  const tiles = new Map();

  // Hong Kong Mahjong: 144 tiles
  const suits = {
    '萬': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '筒': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '索': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '番子': ['東', '南', '西', '北'],
    '字': ['中', '發', '白'],
  };

  // Create 4 of each suit/value combination
  Object.entries(suits).forEach(([suit, values]) => {
    values.forEach(value => {
      for (let i = 0; i < 4; i++) {
        const key = `${suit}_${value}_${i}`;
        const tile = createMahjongTile(scene, suit, value, {
          x: Math.random() * 10 - 5,
          y: Math.random() * 10 - 5,
          z: 0,
        });
        tiles.set(key, tile);
      }
    });
  });

  // Flowers (花) - 8 tiles
  const flowers = ['春', '夏', '秋', '冬', '梅', '蘭', '菊', '竹'];
  flowers.forEach((flower, i) => {
    const key = `花_${flower}_0`;
    const tile = createMahjongTile(scene, '花', flower);
    tiles.set(key, tile);
  });

  // Seasons (季) - 4 tiles
  const seasons = ['一', '二', '三', '四'];
  seasons.forEach((season, i) => {
    const key = `季_${season}_0`;
    const tile = createMahjongTile(scene, '季', season);
    tiles.set(key, tile);
  });

  return tiles;
}

export default {
  createMahjongTile,
  getTileTexturePath,
  createMahjongSet,
};
