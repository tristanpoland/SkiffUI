/**
 * The nodes selection rectangle gets displayed when a user
 * made a selection with on or several nodes
 */
import React, { MouseEvent } from 'react';
import { Node } from '../../types';
export interface NodesSelectionProps {
    onSelectionDragStart?: (event: MouseEvent, nodes: Node[]) => void;
    onSelectionDrag?: (event: MouseEvent, nodes: Node[]) => void;
    onSelectionDragStop?: (event: MouseEvent, nodes: Node[]) => void;
    onSelectionContextMenu?: (event: MouseEvent, nodes: Node[]) => void;
    noPanClassName?: string;
}
declare function NodesSelection({ onSelectionDragStart, onSelectionDrag, onSelectionDragStop, onSelectionContextMenu, noPanClassName, }: NodesSelectionProps): JSX.Element | null;
declare const _default: React.MemoExoticComponent<typeof NodesSelection>;
export default _default;
