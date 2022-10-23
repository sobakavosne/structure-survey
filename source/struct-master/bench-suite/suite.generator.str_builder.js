const H = require('../../../utils/general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)

/**
 * @param {String} root 
 * @param {String} structName 
 * @param {String} fncName
 */
const logDirBuilder =
  (root, structName, fncName) =>
    `${root}/../../log/${structName}/${fncName}/${ENV.STRUCT_MAX}`

/**
* @param {String} root 
* @param {String} fncName 
* @param {String} library 
* @param {Number} iterations 
* @param {Number} structSize 
* @param {String} structName 
*/
const logFileNameBuilder =
  (root, fncName, library, iterations, structSize, structName) =>
    `${root}/../../log/${structName}/${fncName}/${ENV.STRUCT_MAX}`.concat(
      `/{"fnc":"${fncName}","lib":"${library}","iter":${iterations},"size":${structSize}}`
    )

module.exports = {
  logFileNameBuilder,
  logDirBuilder
}