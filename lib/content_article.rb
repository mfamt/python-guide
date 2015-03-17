class ContentArticle
  attr_reader :title, :description, :ordernum, :tldr, :takeaway
  attr_reader :slug, :scope_slug, :collection_slug, :article_slug, :url, :path
  def initialize(resource)
    @url    = resource.url
    @path   = resource.path

    @slug = ContentArticle.slugify(@path)
    @scope_slug = ContentArticle.slugify_scope(@path)
    @collection_slug = ContentArticle.slugify_collection(@path)
    @article_slug = ContentArticle.slugify_article(@path)

    @title  = resource.data.title
    @ordernum = resource.data.ordernum

    @description = resource.data.description
    @tldr = resource.data.tldr
    @takeaway = resource.data.takeaway
  end

  def scope_title
    @scope.capitalize
  end

  # if scope is "lessons", returns "/lessons"
  # if scope is "recipes/informal", returns "/recipes/informal"
  # TODO: the term "scope" is inconsistent here...this is
  #  the full scope needed to resolve the path
  def scope_url
    File.dirname(@url)
  end

  # strip '.html' and leading, trailing slashes
  # "/lessons/file-io.html" => 'lessons/file-io'
  def self.slugify(path)
    path.strip.sub(/\.html$/, '').sub(/^\//, '').sub(/\/$/, '')
  end


  # returns the content subdirectory
  # '/content/lessons/datastuff/file-io.html' => 'lessons'
  # '/content/recipes/practical/whatev.html' => 'recipes'
  def self.slugify_scope(path)
    slugify(path).split('/')[-3]
  end

  # returns the content sub-subdirectory
  # '/content/lessons/datastuff/file-io.html' => 'lessons'
  # '/content/recipes/practical/whatev.html' => 'practical'
  def self.slugify_collection(path)
    slugify(path).split('/')[-2]
  end

  def self.slugify_article(path)
    slugify(path).split('/')[-1]
  end
end

def ContentArticle(obj)
  ContentArticle.new(obj)
end
