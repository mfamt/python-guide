
def make_markdown(str)
  Kramdown::Document.new(str.to_s).to_html
end


def include_code_snippet(fpath, opts = {})
  fname = File.join("code/", fpath)
  raw_content = get_raw_content_from_file(fname)
  splits = raw_content.split(/^# ----$/)
  if splits.count > 1
    polished_content = splits[1..-1].join("\n# ----\n").strip
  else
    polished_content = raw_content
  end

 partial "/layouts/partials/code_snippet",
   locals: { content: polished_content, path: fname, url: fname }

#  partial "/layouts/partials/code_snippet",
#    locals: { content: polished_content, path: resource.path, url: resource.url }
end


# hacky!
# was having trouble with getting files in /code
def get_raw_content_from_file(path)
  if contains_leading_underscore?(path)
    # attempt absolute path
    z = File.expand_path(path, sitemap.app.source_dir)
    File.read(z)
  else
    sitemap.find_resource_by_path(path).render
  end
end


def contains_leading_underscore?(path)
  path.to_s.split('/').any?{|p| p =~ /^_/ }
end
