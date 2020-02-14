import React, { Component } from "react";

export class Map extends Component {
    render() {
        return (
            <>
                <div className="text-center">
                    <object
                        id="map"
                        className="rounded"
                        width="65%"
                        data={
                            "https://bluedonut.space/svg/Universe.svg?&path=" +
                            this.props.route.dotlan_path
                        }
                        type="image/svg+xml"
                    ></object>
                </div>
            </>
        );
    }
}

export default Map;
