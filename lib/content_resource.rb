class ContentResource
  attr_reader :title, :description, :ordernum, :tldr, :takeaway
  attr_reader :slug, :scope, :url, :path
  def initialize(resource)
    @url    = resource.url
    @path   = resource.path
    @slug = ContentResource.slugify(@path)
    @scope = ContentResource.scopify(@path)

    @title  = resource.data.title
    @ordernum = resource.data.ordernum

    @description = resource.data.description
    @tldr = resource.data.tldr
    @takeaway = resource.data.takeaway
  end

  def scope_title
    @scope.capitalize
  end

  # if scope is "chapters", returns "/chapters"
  # if scope is "recipes/informal", returns "/recipes/informal"
  # TODO: the term "scope" is inconsistent here...this is
  #  the full scope needed to resolve the path
  def scope_url
    File.dirname(@url)
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
