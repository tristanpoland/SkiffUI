import React, { ReactNode } from 'react';
import { GraphViewProps } from '../GraphView';
interface FlowRendererProps extends Omit<GraphViewProps, 'snapToGrid' | 'nodeTypes' | 'edgeTypes' | 'snapGrid' | 'connectionLineType' | 'arrowHeadColor' | 'onlyRenderVisibleElements' | 'selectNodesOnDrag' | 'defaultMarkerColor'> {
    children: ReactNode;
}
declare const _default: React.MemoExoticComponent<{
    ({ children, onPaneClick, onPaneContextMenu, onPaneScroll, deleteKeyCode, onMove, onMoveStart, onMoveEnd, selectionKeyCode, multiSelectionKeyCode, zoomActivationKeyCode, elementsSelectable, zoomOnScroll, zoomOnPinch, panOnScroll, panOnScrollSpeed, panOnScrollMode, zoomOnDoubleClick, panOnDrag, defaultPosition, defaultZoom, preventScrolling, onSelectionDragStart, onSelectionDrag, onSelectionDragStop, onSelectionContextMenu, noWheelClassName, noPanClassName, }: FlowRendererProps): JSX.Element;
    displayName: string;
}>;
export default _default;
