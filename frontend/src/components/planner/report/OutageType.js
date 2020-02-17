import React, { Component } from 'react'

import { Label, Input } from 'reactstrap'

export class OutageType extends Component {
    render() {
        return (
            <>
                <Label for="outageType">Outage Type</Label>
                <Input type="select" name="outageType" id="outageType" value={this.props.value} onChange={this.props.onValueChange}>
                    <option value="offline">Structure is offline</option>
                    <option value="fuel">Structure is out of fuel</option>
                    <option value="incorrect">Route planner connection is incorrect</option>
                    <option value="loopback">In-game route tells you to loop back to old system</option>
                    <option value="missingIngame">The tool is missing a jump gate connection</option>
                    <option value="missingTool">The tool is trying to route me to a gate that doesn't exist</option>
                </Input>
            </>
        )
    }
}

export default OutageType
