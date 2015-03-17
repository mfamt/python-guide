require 'lib/content_article'
class ContentScope
  attr_reader :slug, :collections, :title

  def initialize(the_slug, arr)
    @slug = the_slug
    @title = @slug
    @collections = arr.group_by{ |article|
      article.collection_slug
    }.each_pair.map do |kslug, articles|
      ContentCollection(kslug, articles)
    end
  end


  def each_collection(*args, &blk)
    @collections.each(*args, &blk)
  end

  def get_collection_for_article(article)
    @collections.find{|c| c.slug == article.collection_slug}
  end
end


def ContentScope(s, a)
  ContentScope.new(s, a)
end
