import React, { Component } from 'react'
import { withAlert } from 'react-alert'
import { connect } from 'react-redux';
import PropTypes from 'prop-types'


export class Alerts extends Component {
    static propTypes = {
        error: PropTypes.object.isRequired
    }

    componentDidUpdate(prevProps) {
        const { error, alert } = this.props;
        if (error !== prevProps.error) {
            alert.error(error.msg.detail)
            // if (error.status == 403) alert.error(error.msg.detail)
        }
    }

    render() {
        return (
            <></>
        )
    }
}

const mapStateToProps = state => ({
    error: state.errors
});

export default connect(mapStateToProps)(withAlert()(Alerts));