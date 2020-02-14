import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPopular } from "../../../actions/lists";

import { ListGroup, ListGroupItem } from "reactstrap";

export class Popular extends Component {
    static propTypes = {
        popular: PropTypes.array
    };
    componentDidMount() {
        this.props.getPopular();
    }
    render() {
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.popular.map((system, index) => (
                        <ListGroupItem
                            tag="a"
                            href=""
                            className="py-2"
                            action
                            disabled={system ? false : true}
                            key={index}
                        >
                            {system ? system : "N/A"}
                        </ListGroupItem>
                    ))}
                    <small className="text-muted mt-2">Popular</small>
                </ListGroup>
            </>
        );
    }
}

const mapStateToProps = state => ({
    popular: state.popular.popular
});

export default connect(mapStateToProps, { getPopular })(Popular);
