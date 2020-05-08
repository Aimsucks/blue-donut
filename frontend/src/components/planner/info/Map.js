import React, { Component } from 'react'

export class Map extends Component {
  render () {
    return (
      <>
        <div className='text-center'>
          <object
            id='map'
            className='rounded'
            width='65%'
            data={
              'http://evemaps.dotlan.net/svg/Universe.svg?&path=' +
                            this.props.route.dotlan_path
            }
            type='image/svg+xml'
          />
        </div>
      </>
    )
  }
}

export default Map
