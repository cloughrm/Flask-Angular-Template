'use strict';

var gulp = require('gulp');
var paths = gulp.paths;
var util = require('util');
var browserSync = require('browser-sync');
var middleware = require('./proxy');
var replace = require('gulp-replace');

function browserSyncInit(baseDir, files, browser) {
  browser = browser === undefined ? 'default' : browser;

  var routes = null;
  if(baseDir === paths.src || (util.isArray(baseDir) && baseDir.indexOf(paths.src) !== -1)) {
    routes = {
      '/bower_components': 'bower_components'
    };
  }

  browserSync.instance = browserSync.init(files, {
    startPath: '/',
    open: false,
    server: {
      baseDir: baseDir,
      middleware: middleware,
      routes: routes
    },
    browser: browser
  });
}

gulp.task('config', [], function() {
  gulp.src([paths.src + '/app/config/*.js'])
    .pipe(replace('{{API_URL}}', process.env.PASTRY_API || 'http://localhost:5000'))
    .pipe(gulp.dest(paths.tmp + '/serve/app/config'));
});

gulp.task('serve', ['config', 'watch'], function () {
  browserSyncInit([
    paths.tmp + '/serve',
    paths.src,
    '!' + paths.src + '/config',
  ], [
    paths.tmp + '/serve/{app,components}/**/*.css',
    paths.src + '/{app,components}/**/*.js',
    paths.src + 'src/assets/images/**/*',
    paths.tmp + '/serve/*.html',
    paths.tmp + '/serve/{app,components}/**/*.html',
    paths.src + '/{app,components}/**/*.html'
  ]);
});

gulp.task('serve:dist', ['build'], function () {
  browserSyncInit(paths.dist);
});
