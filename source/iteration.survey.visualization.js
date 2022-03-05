const SURVEY_VISUALIZATION = require('./survey-visualizaiton/survey.visualization')

SURVEY_VISUALIZATION.createBenchGridIO(
  'source/struct-master/number.list.itaration.bench.js'
).on(
  'exit',
  (code, signal) => code === 0
    ? SURVEY_VISUALIZATION
      .visualizeExperimentIO(
        'benchmark-visualizer/benchmark_visualizer.py'
      ) : console.error('Grid creation IO error.')
).on(
  'exit',
  (code, signal) => code === 0
    ? console.log('Well done.')
    : console.error('Visualisation IO error.')
)