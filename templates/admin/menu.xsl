<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>
<xsl:template match="/">
  <div class="navbar navbar-inverse navbar-fixed-top">
    <div class="navbar-inner">
      <div class="container">
        <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>

        <div class="nav-collapse collapse">
          <ul class="nav">
            <li class="dropdown">
              <a href="/share" class="dropdown-toggle" data-toggle="dropdown">
                所有宝贝分类<b class="caret"></b>
              </a>
              <ul class="dropdown-menu cate-menu">
                <li>
                  <div class="cate-list">
                    <a href="/share/cl" class="cate-header" >衣服</a>
                  </div>
                  
                  <xsl:for-each select="categories/clothes">
                    <div class="cate-list">
                       <xsl:element name="a">
                          <xsl:attribute name="href">/share/<xsl:value-of select="type"/>/<xsl:value-of select="id"/></xsl:attribute>
                          <xsl:attribute name="class">cate-header</xsl:attribute>
                          <xsl:value-of select="name"/>
                       </xsl:element>
                       <xsl:for-each select="items/item">
                         <xsl:element name="a">
                            <xsl:attribute name="href">/share/<xsl:value-of select="type"/>/<xsl:value-of select="id"/></xsl:attribute>
                            <xsl:choose>
                                <xsl:when test="ishot=1">
                                    <xsl:element name="span" >
                                        <xsl:attribute name="class">is-hot</xsl:attribute>
                                        <xsl:value-of select="name"/>
                                    </xsl:element>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="name"/>
                                </xsl:otherwise>
                            </xsl:choose>
                         </xsl:element>
                       </xsl:for-each>
                    </div>   
                  </xsl:for-each>
                  
                  <div class="divider"></div>
                 <xsl:for-each select="categories/category">
                    <div class="cate-list">
                       <xsl:element name="a">
                          <xsl:attribute name="href">/share/<xsl:value-of select="type"/>/<xsl:value-of select="id"/></xsl:attribute>
                          <xsl:attribute name="class">cate-header</xsl:attribute>
                          <xsl:value-of select="name"/>
                       </xsl:element>
                       <xsl:for-each select="items/item">
                         <xsl:element name="a">
                            <xsl:attribute name="href">/share/<xsl:value-of select="type"/>/<xsl:value-of select="id"/></xsl:attribute>
                            <xsl:choose>
                                <xsl:when test="ishot=1">
                                    <xsl:element name="span" >
                                    <xsl:attribute name="class">is-hot</xsl:attribute>
                                        <xsl:value-of select="name"/>
                                    </xsl:element>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="name"/>
                                </xsl:otherwise>
                            </xsl:choose>
                         </xsl:element>
                       </xsl:for-each>
                    </div>   
                  </xsl:for-each>
                </li>
              </ul>
            </li>
            <li>
              <a href="/share/cl">衣服</a>
            </li>
            <li>
              <a href="/share/sh">鞋子</a>
            </li>
            <li>
              <a href="/share/ac">配饰</a>
            </li>
            <li>
              <a href="/share/ba">包包</a>
            </li>
            <li>
              <a href="/share/co">美容</a>
            </li>
            <li>
              <a href="/share/ho">家居</a>
            </li>
            <li>
              <a href="/share/cr">创意</a>
            </li>
          </ul>
          <p class="navbar-text pull-right">
            <a href="#myModal" role="button" data-toggle="modal" class="navbar-link" >+分享</a>
            <a href="/account/login" class="navbar-link">登录</a>
            <a href="/account/logout" class="navbar-link">注册</a>
          </p>
        </div>
        <!--/.nav-collapse -->
      </div>

    </div>
  </div>


</xsl:template>
    
</xsl:stylesheet>