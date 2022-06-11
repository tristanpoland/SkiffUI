import React, { useState } from 'react';

import ReactFlow, { useNodesState, useEdgesState, Controls, updateEdge, addEdge, MiniMap, Background, getBezierPath, getEdgeCenter } from 'react-flow-renderer';
import './button_edge.css';
import "./graph.css";



const UpdatableEdge = (props) => {

    const foreignObjectSize = 40;


    const [nodes, setNodes, onNodesChange] = useNodesState(props.initialNodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(props.initialEdges);

    const postDelete = async (idxId) => {
        const edge = props.initialEdges[idxId]
        await fetch('https://serverhackathon.prakshal.repl.co/deleteEdge', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([props.currIdx, edge])
        })
            .then(response => response.json())
            .then(response => { props.setDeployment(response); })
    }

    const onEdgeClick = async (evt, id) => {
        evt.stopPropagation();
        const idxId = Number(id.split("-")[1])
        console.log(props.initialEdges[idxId]);
        await postDelete(idxId)
    };

    function CustomEdge({
        id,
        sourceX,
        sourceY,
        targetX,
        targetY,
        sourcePosition,
        targetPosition,
        style = {},
        markerEnd,
        
    }) {
        const edgePath = getBezierPath({
            sourceX,
            sourceY,
            sourcePosition,
            targetX,
            targetY,
            targetPosition,
        });
        const [edgeCenterX, edgeCenterY] = getEdgeCenter({
            sourceX,
            sourceY,
            targetX,
            targetY,
        });

        return (
            <>
                <path
                    id={id}
                    style={style}
                    className="react-flow__edge-path"
                    d={edgePath}
                    markerEnd={markerEnd}
                />
                <foreignObject
                    width={foreignObjectSize}
                    height={foreignObjectSize}
                    x={edgeCenterX - foreignObjectSize / 2}
                    y={edgeCenterY - foreignObjectSize / 2}
                    className="edgebutton-foreignobject"
                    requiredExtensions="http://www.w3.org/1999/xhtml"
                >
                    <body>
                        <button className="edgebutton" onClick={(event) => onEdgeClick(event, id, sourcePosition, targetPosition)}>
                            ×
                        </button>
                    </body>
                </foreignObject>
            </>
        );
    }

    // gets called after end of edge gets dragged to another source or target
    const onEdgeUpdate = (oldEdge, newConnection) => setEdges((els) => {
        // Make API call here
        return updateEdge(oldEdge, newConnection, els);
    });
    const onConnect = (params) => setEdges((els) => addEdge(params, els));

    return (
        <>
            <div className="backbtn" onClick={() => props.setDeployment(null)}><b>&#8592;&nbsp;&nbsp;Back</b></div>
            <ReactFlow
                nodes={nodes}
                edges={edges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                snapToGrid
                onEdgeUpdate={onEdgeUpdate}
                onConnect={onConnect}
                edgeTypes={{ buttonedge: CustomEdge }}
                fitView
                attributionPosition="top-right"
                style={{ width: "100vw", height: "100vh" }}
            >
                <MiniMap />
                <Controls />
                <Background variant="lines" gap={50} size={0.5} style={{ backgroundColor: "#212121" }} />
            </ReactFlow>
        </>
    );
};

export default UpdatableEdge;
