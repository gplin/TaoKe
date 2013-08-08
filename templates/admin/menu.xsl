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
            <li class="dropdown active">
              <a href="/share" class="dropdown-toggle" data-toggle="dropdown">
                所有宝贝分类<b class="caret"></b>
              </a>
              <ul class="dropdown-menu cate-menu">
                <li>
                  <div class="cate-list">
                    <a href="#" class="cate-header" >衣服</a>
                  </div>
                  
                  <xsl:for-each select="categories/clothes">
                    <div class="cate-list">
                        <a href="#" class="cate-header"><xsl:value-of select="name"/></a>
                       <xsl:for-each select="items/item">
                         <xsl:element name="a">
                            <xsl:attribute name="href">/cate/<xsl:value-of select="id"/></xsl:attribute>
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
                        <a href="#" class="cate-header"><xsl:value-of select="name"/></a>
                       <xsl:for-each select="items/item">
                         <xsl:element name="a">
                            <xsl:attribute name="href">/cate/<xsl:value-of select="id"/></xsl:attribute>
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
              <a href="/share/CL">衣服</a>
            </li>
            <li>
              <a href="/share/SH">鞋子</a>
            </li>
            <li>
              <a href="/share/AC">配饰</a>
            </li>
            <li>
              <a href="/share/BA">包包</a>
            </li>
            <li>
              <a href="/share/HO">家居</a>
            </li>
            <li>
              <a href="/share/CR">创意</a>
            </li>
          </ul>
          <p class="navbar-text pull-right">
            <a href="#myModal" role="button" data-toggle="modal" class="navbar-link" >+分享</a>
            <a href="/login" class="navbar-link">登录</a>
            <a href="/logout" class="navbar-link">注册</a>
          </p>
        </div>
        <!--/.nav-collapse -->
      </div>

    </div>
  </div>


</xsl:template>
    
</xsl:stylesheet>