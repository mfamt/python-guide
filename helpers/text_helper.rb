
def make_markdown(str)
  Kramdown::Document.new(str.to_s).to_html
end


def include_code_snippet(fpath, opts = {})
  fname = File.join("code/", fpath)
  resource = _sitemap_get_resource(fname)
  raw_content = resource.render
  polished_content = raw_content.split(/^# ----$/)[1..-1].join("\n# ----\n").strip


  partial "/layouts/partials/code_snippet",
    locals: { content: polished_content, path: resource.path, url: resource.url }
end


# hacky!
# was having trouble with getting files in /code
def _sitemap_get_resource(spath)
  sitemap.find_resource_by_path(spath)
end
