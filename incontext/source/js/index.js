require('es6-promise').polyfill()
require('isomorphic-fetch')


import {placeHints} from './fetch_hints.js'
placeHints()

import {initialize} from './switch.js'
initialize()
