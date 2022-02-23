require('module-alias/register')

const H = require('@general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const DS_GEN = require('./data.struct.generator')

module.exports = {
  I_LIST: DS_GEN.constructIList(ENV.STRUCT_MAX),
  M_LIST: DS_GEN.constructMList(ENV.STRUCT_MAX),
  N_LIST: DS_GEN.constructNList(ENV.STRUCT_MAX),
  L_LIST: DS_GEN.constructLList(ENV.STRUCT_MAX)
}