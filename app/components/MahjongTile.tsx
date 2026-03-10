/**
 * MahjongTile.tsx
 * 
 * 3D Mahjong Tile Component
 * Proportions: 3:4:2 (width:height:depth)
 * 
 * @param suit - 萬/筒/索/番子 (Characters/Bamboo/Dots/Winds)
 * @param value - 1-9 for numbers, 東/南/西/北/中/發/白 for honors
 * @param isFaceDown - whether the tile is face down (shows blue back)
 * @param onClick - click handler
 */

import React, { useRef, useMemo } from 'react';
import { ThreeEvent } from '@react-three/fiber';
import * as THREE from 'three';

// Tile dimensions (3:4:2 ratio)
const TILE_WIDTH = 0.3;
const TILE_HEIGHT = 0.4;
const TILE_DEPTH = 0.2;

// Suit mapping to folder names
const SUIT_MAP: Record<string, string> = {
  '萬': 'characters',
  '筒': 'dots',
  '索': 'bamboo',
  '番子': 'winds',
  '字': 'honors',
};

// Value mapping for image filenames
const VALUE_MAP: Record<string, string> = {
  '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
  '6': '6', '7': '7', '8': '8', '9': '9',
  '東': 'east', '南': 'south', '西': 'west', '北': 'north',
  '中': 'red', '發': 'green', '白': 'white',
};

interface MahjongTileProps {
  suit: string;
  value: string;
  isFaceDown?: boolean;
  onClick?: (event: ThreeEvent<MouseEvent>) => void;
  position?: [number, number, number];
  rotation?: [number, number, number];
  scale?: number;
  isSelected?: boolean;
  isInteractive?: boolean;
}

export const MahjongTile: React.FC<MahjongTileProps> = ({
  suit,
  value,
  isFaceDown = false,
  onClick,
  position = [0, 0, 0],
  rotation = [0, 0, 0],
  scale = 1,
  isSelected = false,
  isInteractive = true,
}) => {
  const meshRef = useRef<THREE.Mesh>(null);

  // Generate texture path based on suit and value
  const texturePath = useMemo(() => {
    if (isFaceDown) return null;
    
    const suitFolder = SUIT_MAP[suit] || 'characters';
    const valueStr = VALUE_MAP[value] || value;
    
    return `/assets/tiles/${suitFolder}_${valueStr}.png`;
  }, [suit, value, isFaceDown]);

  // Create materials for each face
  const materials = useMemo(() => {
    // Front face (shows the tile pattern)
    const frontMaterial = isFaceDown 
      ? new THREE.MeshStandardMaterial({
          color: 0x1a3a5c, // Deep blue back
          roughness: 0.3,
          metalness: 0.1,
        })
      : new THREE.MeshStandardMaterial({
          color: 0xf8f4eb, // Ivory white
          roughness: 0.4,
          metalness: 0.05,
          // In production, load texture here:
          // map: textureLoader.load(texturePath),
        });

    // Back face (same as front for Mahjong)
    const backMaterial = new THREE.MeshStandardMaterial({
      color: 0xf8f4eb,
      roughness: 0.4,
      metalness: 0.05,
    });

    // Left side (ivory)
    const leftMaterial = new THREE.MeshStandardMaterial({
      color: 0xf0ebe0,
      roughness: 0.5,
      metalness: 0.02,
    });

    // Right side (ivory)
    const rightMaterial = new THREE.MeshStandardMaterial({
      color: 0xf0ebe0,
      roughness: 0.5,
      metalness: 0.02,
    });

    // Top face (ivory)
    const topMaterial = new THREE.MeshStandardMaterial({
      color: 0xf8f4eb,
      roughness: 0.35,
      metalness: 0.05,
    });

    // Bottom face (ivory)
    const bottomMaterial = new THREE.MeshStandardMaterial({
      color: 0xe8e0d0,
      roughness: 0.6,
      metalness: 0.02,
    });

    // Order: +X, -X, +Y, -Y, +Z, -Z
    // For BoxGeometry: right, left, top, bottom, front, back
    return [
      rightMaterial,   // +X (right)
      leftMaterial,    // -X (left)
      topMaterial,     // +Y (top)
      bottomMaterial,  // -Y (bottom)
      frontMaterial,   // +Z (front - shows to player)
      backMaterial,    // -Z (back)
    ];
  }, [isFaceDown]);

  // Hover effect
  const [hovered, setHovered] = React.useState(false);

  return (
    <mesh
      ref={meshRef}
      position={position}
      rotation={rotation}
      scale={scale}
      onClick={onClick}
      onPointerOver={(e) => {
        if (isInteractive) {
          e.stopPropagation();
          setHovered(true);
          document.body.style.cursor = 'pointer';
        }
      }}
      onPointerOut={(e) => {
        if (isInteractive) {
          setHovered(false);
          document.body.style.cursor = 'auto';
        }
      }}
      castShadow
      receiveShadow
    >
      <boxGeometry args={[TILE_WIDTH, TILE_HEIGHT, TILE_DEPTH]} />
      {materials.map((material, index) => (
        <primitive key={index} object={material} attach={`material-${index}`} />
      ))}
      
      {/* Selection glow effect */}
      {isSelected && (
        <mesh position={[0, 0, TILE_DEPTH / 2 + 0.01]}>
          <planeGeometry args={[TILE_WIDTH * 0.9, TILE_HEIGHT * 0.9]} />
          <meshBasicMaterial 
            color={0x00d4ff} 
            transparent 
            opacity={0.3} 
          />
        </mesh>
      )}
      
      {/* Hover highlight */}
      {hovered && !isSelected && (
        <mesh position={[0, 0, TILE_DEPTH / 2 + 0.005]}>
          <planeGeometry args={[TILE_WIDTH * 0.95, TILE_HEIGHT * 0.95]} />
          <meshBasicMaterial 
            color={0xffffff} 
            transparent 
            opacity={0.15} 
          />
        </mesh>
      )}
    </mesh>
  );
};

// Helper function to create tile key for React
export const createTileKey = (suit: string, value: string): string => {
  return `${suit}_${value}`;
};

// Tile type definitions for Hong Kong Mahjong
export const HONG_KONG_MAHJONG_TILES = {
  // Characters (萬子) 1-9
  characters: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
  // Bamboo (索子) 1-9  
  bamboo: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
  // Dots (筒子) 1-9
  dots: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
  // Winds (番子)
  winds: ['東', '南', '西', '北'],
  // Honors (字牌)
  honors: ['中', '發', '白'],
};

export default MahjongTile;
