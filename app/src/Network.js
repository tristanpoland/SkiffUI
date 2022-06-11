import React, { useState, useEffect } from 'react';
import Homepage from './Homepage'
import RenderGraph from './RenderGraph'
import "./graph.css"


const Network = () => {
  // States
  const [numDeployments, setnumDeployments] = useState(-1);
  const [currIdx, setCurrIdx] = useState(-1);
  const [deployment, setDeployment] = useState(null);

  const summary = async () => {
    return await fetch(
      (`https://skiffapi.gameplexsoftware.com`),
      {
        mode: 'no-cors',
        headers: {
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/json',
        }
      }
    )
      .then(response => response.json())
      .then((response) => setnumDeployments(response["count"]))
      .catch((error) => {
        console.log(error)
      })
  }

  useEffect(async () => {
    await summary()
  }, []);

  const postCommand = async (deployment_index) => {
    return await fetch(
      (`deployment?number=${deployment_index}`)
    )
      .then(response => response.json())
      .then((response) => { setDeployment(response); setCurrIdx(deployment_index) })
      .catch((error) => {
        console.log(error)
      })
  }

  if (deployment === null) {
    return <Homepage setnumDeployments={setnumDeployments} postCommand={postCommand} numDeployments={numDeployments} />;
  }

  return (
    <RenderGraph initialNodes={deployment.nodes} initialEdges={deployment.edges} setDeployment={setDeployment} currIdx={currIdx} setCurrIdx={setCurrIdx} />
  );
};

export default Network;
