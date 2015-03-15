class ContentResource
  attr_reader :title, :description, :date, :url, :path, :tldr, :ordernum
  attr_reader :slug, :scope
  def initialize(resource)
    @url    = resource.url
    @path   = resource.path
    @title  = resource.data.title
    @description = resource.data.description
    @tldr = resource.data.tldr
    @ordernum = resource.data.ordernum
    @slug = ContentResource.slugify(@path)
    @scope = ContentResource.scopify(@path)
  end

  # strip '.html' and leading, trailing slashes
  # "/chapters/file-io.html" => 'chapters/file-io'
  def self.slugify(path)
    path.strip.sub(/\.html$/, '').sub(/^\//, '').sub(/\/$/, '')
  end

  # returns the subdirectory
  # '/chapters/file-io.html' => 'chapters'
  # '/recipes/practical/whatev.html' => 'practical'
  def self.scopify(path)
    path.strip.split('/')[-2]
  end
end

def ContentResource(obj)
  ContentResource.new(obj)
end
