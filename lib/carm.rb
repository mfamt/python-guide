require 'lib/content_resource'

class Carm
  def initialize(sitemap)
    @resources = sitemap.resources
  end

  def chapters
    r = @resources.select{ |r| r.path =~ /chapters\// }

    r.map{ |a| ContentResource(a) }.sort_by{|a| a.ordernum.to_i }
  end

  def next_chapter(val)
    idx = get_chapter_index(val)
    c = chapters[idx + 1]

    return c.present? ? c : nil
  end

  def prev_chapter(val)
    idx = get_chapter_index(val)
    c = chapters[idx - 1]

    return c.present? ? c : nil
  end

  def get_content_resource(val)
    case val
    when ContentResource
      val
    when Middleman::Sitemap::Resource
      ContentResource(val)
    else
      # assume it's a string path or ordernum
      if val =~ /\/\w+/ # it's a path
        get_content_resource_by_path(val)
      else
        get_content_resource_by_ordernum(val)
      end
    end
  end


  def self.slugify(path)
    ContentResource.slugify(path)
  end

  private
    # assuming :chapters is an Array
    # returns index of chapter in Array
    def get_chapter_index(val)
      r = get_content_resource(val)
      idx = chapters.index{|c| c.ordernum == r.ordernum }

      return idx
    end

    def get_content_resource_by_ordernum(num)
      onum = num.to_i

      chapters.find{|c| c.ordernum == onum}
    end

    def get_content_resource_by_path(path)
      pslug = Carm.slugify(path)

      chapters.find{|c| c.slug == pslug }
    end
end
