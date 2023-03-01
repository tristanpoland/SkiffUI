import React, { CSSProperties } from 'react';
import { Edge, ConnectionLineType, ConnectionLineComponent, OnEdgeUpdateFunc } from '../../types';
interface EdgeRendererProps {
    edgeTypes: any;
    connectionLineType: ConnectionLineType;
    connectionLineStyle?: CSSProperties;
    connectionLineComponent?: ConnectionLineComponent;
    onEdgeClick?: (event: React.MouseEvent, node: Edge) => void;
    onEdgeDoubleClick?: (event: React.MouseEvent, edge: Edge) => void;
    defaultMarkerColor: string;
    onlyRenderVisibleElements: boolean;
    onEdgeUpdate?: OnEdgeUpdateFunc;
    onEdgeContextMenu?: (event: React.MouseEvent, edge: Edge) => void;
    onEdgeMouseEnter?: (event: React.MouseEvent, edge: Edge) => void;
    onEdgeMouseMove?: (event: React.MouseEvent, edge: Edge) => void;
    onEdgeMouseLeave?: (event: React.MouseEvent, edge: Edge) => void;
    onEdgeUpdateStart?: (event: React.MouseEvent, edge: Edge) => void;
    onEdgeUpdateEnd?: (event: MouseEvent, edge: Edge) => void;
    edgeUpdaterRadius?: number;
    noPanClassName?: string;
}
declare const _default: React.MemoExoticComponent<{
    (props: EdgeRendererProps): JSX.Element | null;
    displayName: string;
}>;
export default _default;
