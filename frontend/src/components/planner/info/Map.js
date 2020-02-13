import React, { Component } from "react";

export class Map extends Component {
    render() {
        return (
            <>
                <object
                    id="map"
                    className="rounded"
                    width="100%"
                    data={
                        "https://bluedonut.space/svg/Universe.svg?&path=" +
                        this.props.route.dotlan_path
                    }
                    type="image/svg+xml"
                ></object>
            </>
        );
    }
}

export default Map;
