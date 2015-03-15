

class ContentResource
  attr_reader :title, :description, :date, :url, :path, :slug, :tldr, :ordernum
  def initialize(resource)
    @url    = resource.url
    @path   = resource.path
    @title  = resource.data.title
    @description = resource.data.description
    @tldr = resource.data.tldr
    @ordernum = resource.data.ordernum
    @slug = ContentResource.slugify(@path)
  end

  # strip '.html' and leading, trailing slashes
  # "/chapters/file-io.html" => 'chapters/file-io'
  def self.slugify(path)
    path.strip.sub(/\.html$/, '').sub(/^\//, '').sub(/\/$/, '')
  end
end

def ContentResource(obj)
  ContentResource.new(obj)
end
