const H = require('../utils/general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const SURVEY_VISUALIZATION = require('./survey-visualizaiton/survey.visualization')

SURVEY_VISUALIZATION.createGeneration(
  'source/struct-master/struct.iteration.benchmark.js',
  ENV.STRUCT_SIZE,
  ENV.STRUCT_GEN_STEP
).on(
  'exit',
  (code, signal) => code === 0
    ? SURVEY_VISUALIZATION.visualizeExperiment('iteration')
    : undefined
)