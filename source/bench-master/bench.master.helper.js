require('module-alias/register')

const H = require('@general-helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const CLI_COLOR = require('cli-color')

/**
 * @param {String} library 
 */
const constructMeanBenchmarkDescription =
  (library) =>
    `\t\t\t: ${library === 'IMMUTABLE.JS'
      ? CLI_COLOR.bgBlueBright(library)
      : library === 'MORI.JS'
        ? CLI_COLOR.bgWhiteBright(library)
        : CLI_COLOR.bgGreenBright(library)
    } EXECUTION MEAN VALUE OF ${ENV.ITERATIONS} ITERATIONS, ${CLI_COLOR.red('ms')}`

module.exports = {
  constructMeanBenchmarkDescription
}
