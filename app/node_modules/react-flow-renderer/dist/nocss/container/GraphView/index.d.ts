import React from 'react';
import { NodeTypes, EdgeTypes, ConnectionLineType, KeyCode, ReactFlowProps } from '../../types';
export interface GraphViewProps extends Omit<ReactFlowProps, 'onSelectionChange' | 'nodes' | 'edges'> {
    nodeTypes: NodeTypes;
    edgeTypes: EdgeTypes;
    selectionKeyCode: KeyCode | null;
    deleteKeyCode: KeyCode | null;
    multiSelectionKeyCode: KeyCode | null;
    connectionLineType: ConnectionLineType;
    onlyRenderVisibleElements: boolean;
    defaultZoom: number;
    defaultPosition: [number, number];
    defaultMarkerColor: string;
    selectNodesOnDrag: boolean;
    noDragClassName: string;
    noWheelClassName: string;
    noPanClassName: string;
}
declare const _default: React.MemoExoticComponent<{
    ({ nodeTypes, edgeTypes, onMove, onMoveStart, onMoveEnd, onInit, onNodeClick, onEdgeClick, onNodeDoubleClick, onEdgeDoubleClick, onNodeMouseEnter, onNodeMouseMove, onNodeMouseLeave, onNodeContextMenu, onNodeDragStart, onNodeDrag, onNodeDragStop, onSelectionDragStart, onSelectionDrag, onSelectionDragStop, onSelectionContextMenu, connectionLineType, connectionLineStyle, connectionLineComponent, selectionKeyCode, multiSelectionKeyCode, zoomActivationKeyCode, deleteKeyCode, onlyRenderVisibleElements, elementsSelectable, selectNodesOnDrag, defaultZoom, defaultPosition, preventScrolling, defaultMarkerColor, zoomOnScroll, zoomOnPinch, panOnScroll, panOnScrollSpeed, panOnScrollMode, zoomOnDoubleClick, panOnDrag, onPaneClick, onPaneScroll, onPaneContextMenu, onEdgeUpdate, onEdgeContextMenu, onEdgeMouseEnter, onEdgeMouseMove, onEdgeMouseLeave, edgeUpdaterRadius, onEdgeUpdateStart, onEdgeUpdateEnd, noDragClassName, noWheelClassName, noPanClassName, }: GraphViewProps): JSX.Element;
    displayName: string;
}>;
export default _default;
