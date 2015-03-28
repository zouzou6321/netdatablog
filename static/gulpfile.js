/**
 * Created by hhy on 2015/3/28.
 */
var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')(),
    browserSync = require('browser-sync');

var config = require('./config.json');

gulp.task('sync', function(){
    browserSync({
        proxy: 'localhost:8000'
    });
});

// 合并文件之后压缩代码
gulp.task('scripts', function (){
     return gulp.src(config.js.src)
        .pipe(plugins.jshint())
        .pipe(plugins.jshint.reporter('default'))
        .pipe(plugins.concat('all.js'))
        .pipe(gulp.dest(config.js.prod))
        .pipe(plugins.uglify())
        .pipe(plugins.rename('all.min.js'))
        .pipe(gulp.dest(config.js.prod))
        .pipe(plugins.notify({ message: 'Scripts task complete' }));
});

//样式文件处理
gulp.task('styles', function() {
    return gulp.src(config.css.src)
        .pipe(plugins.sass({ style: 'expanded' }))
        .pipe(plugins.autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
        .pipe(gulp.dest(config.css.prod))
        .pipe(plugins.rename({suffix: '.min'}))
        .pipe(plugins.minifyCss())
        .pipe(gulp.dest(config.css.prod))
        .pipe(plugins.notify({ message: 'Styles task complete' }));
});

// 图片
gulp.task('images', function() {
  return gulp.src(config.imgs.src)
    .pipe(plugins.cache(plugins.imagemin({ optimizationLevel: 3, progressive: true, interlaced: true })))
    .pipe(gulp.dest(config.imgs.prod))
    .pipe(plugins.notify({ message: 'Images task complete' }));
});

// 清理
gulp.task('clean', function() {
  return gulp.src([config.js.prod, config.css.prod, config.imgs.prod], {read: false})
    .pipe(plugins.clean());
});

// 监视文件的变化
gulp.task('watch', function () {
    gulp.watch(config.js.src, ['scripts']);
    gulp.watch(config.css.src, ['styles']);
    gulp.watch(config.imgs.src, ['images']);
});

// 注册缺省任务
// 预设任务
gulp.task('default', ['clean'], function() {
    gulp.start('styles', 'scripts', 'images');
});
