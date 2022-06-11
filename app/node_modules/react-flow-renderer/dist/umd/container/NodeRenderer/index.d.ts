import React, { MouseEvent } from 'react';
import { Node, NodeTypes } from '../../types';
interface NodeRendererProps {
    nodeTypes: NodeTypes;
    selectNodesOnDrag: boolean;
    onNodeClick?: (event: MouseEvent, element: Node) => void;
    onNodeDoubleClick?: (event: MouseEvent, element: Node) => void;
    onNodeMouseEnter?: (event: MouseEvent, node: Node) => void;
    onNodeMouseMove?: (event: MouseEvent, node: Node) => void;
    onNodeMouseLeave?: (event: MouseEvent, node: Node) => void;
    onNodeContextMenu?: (event: MouseEvent, node: Node) => void;
    onNodeDragStart?: (event: MouseEvent, node: Node) => void;
    onNodeDrag?: (event: MouseEvent, node: Node) => void;
    onNodeDragStop?: (event: MouseEvent, node: Node) => void;
    onlyRenderVisibleElements: boolean;
    noPanClassName: string;
    noDragClassName: string;
}
declare const _default: React.MemoExoticComponent<{
    (props: NodeRendererProps): JSX.Element;
    displayName: string;
}>;
export default _default;
