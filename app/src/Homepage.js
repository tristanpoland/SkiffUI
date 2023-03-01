import React, { Component } from 'react';
import { Card, Row, Col, Dropdown } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Hero from "./images/Hero.jpeg"
import "./homepage.css"

class Homepage extends Component {
    constructor(props) {
        super(props);
    }

    renderNumDeployments = () => {
        if (this.props.numDeployments === -1) {
            return <Dropdown.Item>Loading...</Dropdown.Item>
        }
        const deployments = [];
        for (let i = 0; i < this.props.numDeployments; i++) {
            deployments.push(<Dropdown.Item onClick={() => { this.props.postCommand(i) }} key={`dep_${i}`}>Deployment {i + 1}</Dropdown.Item>)
        }
        return deployments;
    }

    render() {
        return (
            <div style={{ backgroundImage: `url('https://i.pinimg.com/originals/06/cf/4d/06cf4d458599c0b375204b82391b9817.jpg')`, height: "100vh", backgroundPosition: "center", backgroundSize: "cover" }}>
                <Row className="d-flex justify-content-center min-vh-50">
                    <Col xs={12} lg={9} className="mt-5">
                        <Card className="m-4 h-100 mt-5 bg-opacity-75 text-center gradient_card" bg="dark" text="light">
                            <Card.Header><h1>Skiff</h1></Card.Header>
                            <Card.Body>
                                <h3>Simplicity is the Ultimate Sophistication --leonardo da vinci</h3>
                                <p className="m-3">
                                    Skiff is graphical drag-and-drop tool for configuring/connecting interfaces on Docker containers.
                                    <br />
                                    Our mission is to make docker commands and networking incredibly simple.
                                    So that anyone can do in <label className="text-warning">minutes</label>. what used to take <label className="text-warning">hours</label>...
                                </p>

                                <Row className="m-4">
                                    <Col>
                                        <Dropdown>
                                            <Dropdown.Toggle variant="outline-warning" id="dropdown-basic">
                                                Select Deployments
                                            </Dropdown.Toggle>

                                            <Dropdown.Menu>
                                                {this.renderNumDeployments()}
                                            </Dropdown.Menu>
                                        </Dropdown>
                                    </Col>
                                </Row>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        )
    }
}

export default Homepage

// style={{position: "fixed", bottom: "0px", width: "100%", height: "28px", backgroundColor: "#333"}}