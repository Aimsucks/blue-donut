import React, { Component } from "react";

export class Splash extends Component {
    render() {
        const splashStyle = {
            background: "url('/static/img/donut.png')",
            backgroundSize: "750px",
            backgroundRepeat: "no-repeat",
            backgroundPosition: "center 30px"
        };

        return (
            <>
                <div className="bg-primary py-5" style={splashStyle}>
                    <div className="text-center py-5">
                        <h1 className="display-3 mb-0">Blue Donut</h1>
                        <p className="lead">
                            Tools to help you live in the blue donut
                        </p>
                    </div>
                </div>
            </>
        );
    }
}

// /static/img/donut.png

export default Splash;
