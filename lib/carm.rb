class Carm
  def initialize(sitemap)
    @resources = sitemap.resources
  end

  def chapters
    r = @resources.select{ |r| r.path =~ /chapters\// }

    r.map{ |a| ContentResource.new(a) }.sort_by{|a| a.order.to_i }
  end
end


class ContentResource
  attr_reader :title, :description, :date, :url, :path, :slug, :tldr, :order
  def initialize(resource)
    @url    = resource.url
    @path   = resource.path
    @title  = resource.data.title
    @slug   = File.basename(@path).gsub(/\.\w{2,4}$/, '')
    @description = resource.data.description
    @tldr = resource.data.tldr
    @order = resource.data.order
  end
end
