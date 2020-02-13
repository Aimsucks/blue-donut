import React, { Component } from "react";

import { Button } from "reactstrap";

export class Map extends Component {
    render() {
        return (
            <>
                <h2 className="text-center mb-0">
                    {this.props.route.destination}
                </h2>
                <p class="mb-2 text-muted text-center">
                    {this.props.route.length} jumps
                </p>
                <Button block color="primary">
                    Set destination
                </Button>
                <Button block color="secondary">
                    Copy sharable link
                </Button>
            </>
        );
    }
}

export default Map;
