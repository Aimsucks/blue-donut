import React, { Component } from "react";

import { ListGroup, ListGroupItem } from "reactstrap";

export class Recents extends Component {
    render() {
        return (
            <>
                <ListGroup className="text-center">
                    <ListGroupItem tag="a" href="" className="py-2" action>
                        D-PNP9
                    </ListGroupItem>
                    <ListGroupItem tag="a" href="" className="py-2" action>
                        D-PNP9
                    </ListGroupItem>
                    <ListGroupItem tag="a" href="" className="py-2" action>
                        D-PNP9
                    </ListGroupItem>
                    <ListGroupItem tag="a" href="" className="py-2" action>
                        D-PNP9
                    </ListGroupItem>
                    <ListGroupItem tag="a" href="" className="py-2" action>
                        D-PNP9
                    </ListGroupItem>
                    <small className="text-muted mt-2">Recents</small>
                </ListGroup>
            </>
        );
    }
}

export default Recents;
