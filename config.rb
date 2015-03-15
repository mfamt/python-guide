require 'lib/carm'

activate :livereload
activate :i18n, :mount_at_root => :en
activate :directory_indexes

set :markdown_engine, :kramdown
set :trailing_slash, true
set :css_dir, 'stylesheets'
set :js_dir, 'javascripts'
set :images_dir, 'images'

# set :css_dir, 'assets/stylesheets'
# set :js_dir, 'assets/javascripts'
# set :images_dir, 'assets/images'

# Build-specific configuration
configure :build do

end
