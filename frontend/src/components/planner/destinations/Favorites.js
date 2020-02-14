import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getFavorites } from "../../../actions/lists";

import { ListGroup, ListGroupItem } from "reactstrap";

export class Favorites extends Component {
    static propTypes = {
        favorites: PropTypes.array
    };
    componentDidMount() {
        this.props.getFavorites();
    }
    render() {
        console.log(this.props.favorites);
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.favorites.map((system, index) => (
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
                    <small className="text-muted mt-2">Favorites</small>
                </ListGroup>
            </>
        );
    }
}

const mapStateToProps = state => ({
    favorites: state.favorites.favorites
});

export default connect(mapStateToProps, { getFavorites })(Favorites);
