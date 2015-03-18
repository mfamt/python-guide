require 'lib/content_article'
class ContentScope
  attr_reader :slug, :collections, :title, :description

  def initialize(the_slug, obj, all_articles)
    @slug = the_slug
    @title = obj.title
    @title = obj.description
    @collections = obj.collections.each_pair.map do |col_slug, col_obj|
      col_articles = all_articles.select{|a| a.collection_slug == col_slug }
      ContentCollection(col_slug, col_obj, col_articles)
    end
  end


  def each_collection(*args, &blk)
    @collections.each(*args, &blk)
  end

  def get_collection_for_article(article)
    @collections.find{|c| c.slug == article.collection_slug}
  end
end


def ContentScope(s, obj, a)
  ContentScope.new(s, obj, a)
end
