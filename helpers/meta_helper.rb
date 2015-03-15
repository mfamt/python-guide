def page_title
  data_title = current_page.data.title
  if data_title.blank?
    config[:site_title]
  elsif data_title == config[:site_title]
    "#{config[:site_deck]} | #{config[:site_title]}"
  else
    "#{data_title} | #{config[:site_title]}"
  end
end



def page_description
  current_page.data.description || config[:site_description]
end


def current_lede_image_url
  if (m = current_page.data.metax)
    if (img = m.lede_image)
      return img
    end
  end
end

def current_lede_image_caption
  if (m = current_page.data.metax)
    if (txt = m.lede_caption)
      return make_markdown txt
    end
  end
end
