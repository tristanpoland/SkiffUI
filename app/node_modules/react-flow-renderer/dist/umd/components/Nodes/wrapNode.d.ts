import React, { ComponentType } from 'react';
import { NodeProps, WrapNodeProps } from '../../types';
declare const _default: (NodeComponent: ComponentType<NodeProps>) => React.MemoExoticComponent<{
    ({ id, type, data, scale, xPos, yPos, selected, onClick, onMouseEnter, onMouseMove, onMouseLeave, onContextMenu, onNodeDoubleClick, onNodeDragStart, onNodeDrag, onNodeDragStop, style, className, isDraggable, isSelectable, isConnectable, selectNodesOnDrag, sourcePosition, targetPosition, hidden, snapToGrid, snapGrid, dragging, resizeObserver, dragHandle, zIndex, isParent, noPanClassName, noDragClassName, }: WrapNodeProps): JSX.Element | null;
    displayName: string;
}>;
export default _default;
