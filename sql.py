



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>SQL-optimizer/sql.py at master · hgautham/SQL-optimizer</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="hgautham/SQL-optimizer" name="twitter:title" /><meta content="Contribute to SQL-optimizer development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/9004151?v=3&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/9004151?v=3&amp;s=400" property="og:image" /><meta content="hgautham/SQL-optimizer" property="og:title" /><meta content="https://github.com/hgautham/SQL-optimizer" property="og:url" /><meta content="Contribute to SQL-optimizer development by creating an account on GitHub." property="og:description" />

      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="40FB9520:0F94:26C4F69:547BC7BD" name="octolytics-dimension-request_id" /><meta content="9004151" name="octolytics-actor-id" /><meta content="hgautham" name="octolytics-actor-login" /><meta content="768f82f18b8ad8191925223a7d9dde8137441920f0f674ef0ea78bde13d25d76" name="octolytics-actor-hash" />
    <meta content="/private/private/blob/show" name="analytics-location" />
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="37LC3H3v8RFWT8NzGhY6urjFzHv+O1U9qbZkYy3853P/zqtb6g/+4ryKSSULUZxktnBdiRKiQvfA/Eg6Z2jJLQ==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-5561576deeeba73b1c76a1de3c562f5d65ee6ea990aa632c3b75c3a7c811ea3a.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-8b922a51411bd139fd6c83861e8c0a4568e7192869563d83ffadaca58d30b0b0.css" media="all" rel="stylesheet" type="text/css" />
    
    


    <meta http-equiv="x-pjax-version" content="d3b3e83d2bcdc99c3934dada18652b80">

      
  <meta name="description" content="Contribute to SQL-optimizer development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/hgautham/SQL-optimizer git https://github.com/hgautham/SQL-optimizer.git">

  <meta content="9004151" name="octolytics-dimension-user_id" /><meta content="hgautham" name="octolytics-dimension-user_login" /><meta content="27355559" name="octolytics-dimension-repository_id" /><meta content="hgautham/SQL-optimizer" name="octolytics-dimension-repository_nwo" /><meta content="false" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="27355559" name="octolytics-dimension-repository_network_root_id" /><meta content="hgautham/SQL-optimizer" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/hgautham/SQL-optimizer/commits/master.atom?token=AIlkd_hAaV9simKBp_Zvpwf8AJ1RXT4Eks6yiPpBwA%3D%3D" rel="alternate" title="Recent Commits to SQL-optimizer:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-private page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/hgautham/SQL-optimizer/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/hgautham/SQL-optimizer/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/hgautham" data-ga-click="Header, go to profile, text:username">
      <img alt="hgautham" class="avatar" data-user="9004151" height="20" src="https://avatars0.githubusercontent.com/u/9004151?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">hgautham</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="hgautham/SQL-optimizer">This repository</span>
    </li>
      <li>
        <a href="/hgautham/SQL-optimizer/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/hgautham/SQL-optimizer/settings/collaboration"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="GRguu1xHWZf99bCY+OUTIFsy1UCzXZ6IpG1mnKuSQJy+kllOhtmZE1d/1yu+d9dxTKqnoVbrL9AHDjGfdsMJtQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="sLsNKNb5dIXWNPNVW3aXVo/MwX8dT9PgYetLKl89K0bCcLBN04LEV+IWUDyasUG3PcTjwuBIc9KwKeuLMPIBuQ==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="27355559" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/hgautham/SQL-optimizer/watchers">
        1
      </a>
      <a href="/hgautham/SQL-optimizer/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Unwatch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/hgautham/SQL-optimizer/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="etN2ULk47GZjDOOKv5BR2+KsRIfhObjIMXnA1nKZm7enNnSXPdLANClh1DWRiMZvCxom+ELgk5eWxL7EYAvTtg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar hgautham/SQL-optimizer">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/hgautham/SQL-optimizer/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/hgautham/SQL-optimizer/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="UbukncZ2kQeskUu00TtwrkHS1EIXrlHpMjMUKd5x1vp3lq8gWAMELUiuqMVFkq3fcmOi+Bi9/NiCP7xprQRgBA==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star hgautham/SQL-optimizer">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/hgautham/SQL-optimizer/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/hgautham/SQL-optimizer/fork" class="minibutton with-count js-toggler-target fork-button tooltipped-n" title="Fork your own copy of hgautham/SQL-optimizer to your account" aria-label="Fork your own copy of hgautham/SQL-optimizer to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/hgautham/SQL-optimizer/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title private">
          <span class="mega-octicon octicon-lock"></span>
          <span class="author"><a href="/hgautham" class="url fn" itemprop="url" rel="author"><span itemprop="title">hgautham</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/hgautham/SQL-optimizer" class="js-current-repository" data-pjax="#js-repo-pjax-container">SQL-optimizer</a></strong>
            <span class="repo-private-label">private</span>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/hgautham/SQL-optimizer/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/hgautham/SQL-optimizer" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /hgautham/SQL-optimizer">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/hgautham/SQL-optimizer/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /hgautham/SQL-optimizer/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/hgautham/SQL-optimizer/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /hgautham/SQL-optimizer/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/hgautham/SQL-optimizer/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /hgautham/SQL-optimizer/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/hgautham/SQL-optimizer/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /hgautham/SQL-optimizer/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/hgautham/SQL-optimizer/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /hgautham/SQL-optimizer/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/hgautham/SQL-optimizer/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /hgautham/SQL-optimizer/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/hgautham/SQL-optimizer.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hgautham/SQL-optimizer.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="git@github.com:hgautham/SQL-optimizer.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:hgautham/SQL-optimizer.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/hgautham/SQL-optimizer" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hgautham/SQL-optimizer" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/hgautham/SQL-optimizer" class="minibutton sidebar-button" title="Save hgautham/SQL-optimizer to your computer and use it in GitHub Desktop." aria-label="Save hgautham/SQL-optimizer to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/hgautham/SQL-optimizer/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of hgautham/SQL-optimizer as a zip file"
                   title="Download the contents of hgautham/SQL-optimizer as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/hgautham/SQL-optimizer/blob/97752198fdce54c2df7e2490f1a2c1067e7a7ab6/sql.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:b02d5ce7e0f7dc61fcdf0ba31b96e1a7 -->

<div class="file-navigation">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/hgautham/SQL-optimizer/blob/master/sql.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/hgautham/SQL-optimizer/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="hGqsBHAR+igSOR0N61a3NQgbm5jKs83+tJmJk4Rhz0UtLoIPamZ2f4JRIl/qtJ3c+v6BqO2hGNIvEJHES+IYDg==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="sql.py">
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/hgautham/SQL-optimizer/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="sql.py" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hgautham/SQL-optimizer" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">SQL-optimizer</span></a></span></span><span class="separator"> / </span><strong class="final-path">sql.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/hgautham/SQL-optimizer/contributors/master/sql.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>87 lines (74 sloc)</span>
          <span class="meta-divider"></span>
        <span>3.762 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/hgautham/SQL-optimizer/raw/master/sql.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/hgautham/SQL-optimizer/blame/master/sql.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/hgautham/SQL-optimizer/commits/master/sql.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="github-windows://openRepo/https://github.com/hgautham/SQL-optimizer?branch=master&amp;filepath=sql.py" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button js-update-url-with-hash"
                 href="/hgautham/SQL-optimizer/edit/master/sql.py"
                 aria-label="Edit this file"
                 data-method="post" rel="nofollow" data-hotkey="e"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger"
               href="/hgautham/SQL-optimizer/delete/master/sql.py"
               aria-label="Delete this file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-k">from</span> pyparsing <span class="pl-k">import</span> Literal, CaselessLiteral, Word, Upcase, delimitedList, Optional, \</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line">    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line">    ZeroOrMore, restOfLine, Keyword</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">test</span>( <span class="pl-vpf">str</span> ):</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">    <span class="pl-k">print</span> <span class="pl-s3">str</span>,<span class="pl-s1"><span class="pl-pds">&quot;</span>-&gt;<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">        tokens <span class="pl-k">=</span> simpleSQL.parseString( <span class="pl-s3">str</span> )</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>tokens = <span class="pl-pds">&quot;</span></span>,        tokens</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>tokens.columns =<span class="pl-pds">&quot;</span></span>, tokens.columns</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>tokens.tables =<span class="pl-pds">&quot;</span></span>,  tokens.tables</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>tokens.where =<span class="pl-pds">&quot;</span></span>, tokens.where</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>tokens.tableAlias =<span class="pl-pds">&quot;</span></span>, tokens.tablealias</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">    <span class="pl-k">except</span> ParseException, err:</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span><span class="pl-k">*</span>err.loc <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>^<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> err.msg</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">        <span class="pl-k">print</span> err</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">    <span class="pl-k">print</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line"><span class="pl-c"># define SQL tokens</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">selectStmt <span class="pl-k">=</span> Forward()</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">selectToken <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>select<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">fromToken   <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>from<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">astoken  <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>AS<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line">ident          <span class="pl-k">=</span> Word( alphas, alphanums <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>_$<span class="pl-pds">&quot;</span></span> ).setName(<span class="pl-s1"><span class="pl-pds">&quot;</span>identifier<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">columnName     <span class="pl-k">=</span> Upcase( delimitedList( ident, <span class="pl-s1"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">combine</span><span class="pl-k">=</span><span class="pl-c1">True</span> ) )</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">columnNameList <span class="pl-k">=</span> Group( delimitedList( columnName ) )</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">tableName      <span class="pl-k">=</span> Upcase( delimitedList( ident, <span class="pl-s1"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">combine</span><span class="pl-k">=</span><span class="pl-c1">True</span> ) )</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">tableName2      <span class="pl-k">=</span> Upcase( delimitedList( ident, <span class="pl-s1"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">combine</span><span class="pl-k">=</span><span class="pl-c1">True</span> ) )</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">tableAlias  <span class="pl-k">=</span> tableName <span class="pl-k">+</span> astoken <span class="pl-k">+</span> tableName2.setName( <span class="pl-s1"><span class="pl-pds">&quot;</span>tablealias<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">tableNameList  <span class="pl-k">=</span> Group( delimitedList( tableAlias <span class="pl-k">|</span> tableName ) )</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">whereExpression <span class="pl-k">=</span> Forward()</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">and_ <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>and<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">or_ <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>or<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">in_ <span class="pl-k">=</span> Keyword(<span class="pl-s1"><span class="pl-pds">&quot;</span>in<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">E <span class="pl-k">=</span> CaselessLiteral(<span class="pl-s1"><span class="pl-pds">&quot;</span>E<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">binop <span class="pl-k">=</span> oneOf(<span class="pl-s1"><span class="pl-pds">&quot;</span>= != &lt; &gt; &gt;= &lt;= eq ne lt le gt ge<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">caseless</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">arithSign <span class="pl-k">=</span> Word(<span class="pl-s1"><span class="pl-pds">&quot;</span>+-<span class="pl-pds">&quot;</span></span>,<span class="pl-vpf">exact</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">realNum <span class="pl-k">=</span> Combine( Optional(arithSign) <span class="pl-k">+</span> ( Word( nums ) <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> Optional( Word(nums) )  <span class="pl-k">|</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">                                                         ( <span class="pl-s1"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> Word(nums) ) ) <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">            Optional( E <span class="pl-k">+</span> Optional(arithSign) <span class="pl-k">+</span> Word(nums) ) )</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">intNum <span class="pl-k">=</span> Combine( Optional(arithSign) <span class="pl-k">+</span> Word( nums ) <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">            Optional( E <span class="pl-k">+</span> Optional(<span class="pl-s1"><span class="pl-pds">&quot;</span>+<span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> Word(nums) ) )</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">columnRval <span class="pl-k">=</span> realNum <span class="pl-k">|</span> intNum <span class="pl-k">|</span> quotedString <span class="pl-k">|</span> columnName <span class="pl-c"># need to add support for alg expressions</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">whereCondition <span class="pl-k">=</span> Group(</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">    ( columnName <span class="pl-k">+</span> binop <span class="pl-k">+</span> columnRval ) <span class="pl-k">|</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">    ( columnName <span class="pl-k">+</span> in_ <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> delimitedList( columnRval ) <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>)<span class="pl-pds">&quot;</span></span> ) <span class="pl-k">|</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">    ( columnName <span class="pl-k">+</span> in_ <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> selectStmt <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>)<span class="pl-pds">&quot;</span></span> ) <span class="pl-k">|</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">    ( <span class="pl-s1"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> whereExpression <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>)<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">whereExpression <span class="pl-k">&lt;&lt;</span> whereCondition <span class="pl-k">+</span> ZeroOrMore( ( and_ <span class="pl-k">|</span> or_ ) <span class="pl-k">+</span> whereExpression ) </td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line"><span class="pl-c"># define the grammar</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">selectStmt      <span class="pl-k">&lt;&lt;</span> ( selectToken <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">                   ( <span class="pl-s1"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span> <span class="pl-k">|</span> columnNameList ).setResultsName( <span class="pl-s1"><span class="pl-pds">&quot;</span>columns<span class="pl-pds">&quot;</span></span> ) <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">                   fromToken <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">                   tableNameList.setResultsName( <span class="pl-s1"><span class="pl-pds">&quot;</span>tables<span class="pl-pds">&quot;</span></span> ) <span class="pl-k">+</span> </td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">                   Optional( Group( CaselessLiteral(<span class="pl-s1"><span class="pl-pds">&quot;</span>where<span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> whereExpression ), <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> ).setResultsName(<span class="pl-s1"><span class="pl-pds">&quot;</span>where<span class="pl-pds">&quot;</span></span>) )</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">simpleSQL <span class="pl-k">=</span> selectStmt</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line"><span class="pl-c"># define Oracle comment format, and ignore them</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">oracleSqlComment <span class="pl-k">=</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>--<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> restOfLine</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">simpleSQL.ignore( oracleSqlComment )</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-k">SELECT</span> <span class="pl-k">*</span> <span class="pl-k">from</span> XYZZY, ABC<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>select * from SYS.XYZZY<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A from Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A,B,C from Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A, B, C from Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A, B, C from Sys.dual, Table2   <span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Xelect A, B, C from Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A, B, C frox Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select &amp;&amp;&amp; frox Sys.dual<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A from Sys.dual where a in (&#39;RED&#39;,&#39;GREEN&#39;,&#39;BLUE&#39;)<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A from Sys.dual where a in (&#39;RED&#39;,&#39;GREEN&#39;,&#39;BLUE&#39;) and b in (10,20,30)<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">test( <span class="pl-s1"><span class="pl-pds">&quot;</span>Select A,b from table1,table2 where table1.id = table2.id -- test out comparison operators<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">test(<span class="pl-s1"><span class="pl-pds">&quot;</span>Select S.sname from Sailors AS S,Reserves AS R where S.sid=R.sid and R.bid=103<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">test(<span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-k">SELECT</span> <span class="pl-c1">S</span>.<span class="pl-c1">sname</span> <span class="pl-k">FROM</span> Sailors <span class="pl-k">AS</span> S, Reserves <span class="pl-k">AS</span> R, Boats <span class="pl-k">AS</span> B <span class="pl-k">WHERE</span> <span class="pl-c1">S</span>.<span class="pl-c1">sid</span><span class="pl-k">=</span><span class="pl-c1">R</span>.<span class="pl-c1">sid</span> <span class="pl-k">AND</span> <span class="pl-c1">R</span>.<span class="pl-c1">bid</span><span class="pl-k">=</span><span class="pl-c1">B</span>.<span class="pl-c1">bid</span> <span class="pl-k">AND</span> <span class="pl-c1">B</span>.<span class="pl-c1">color</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>red<span class="pl-pds">&#39;</span></span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">test(<span class="pl-s1"><span class="pl-pds">&quot;</span>Select S.sname from Sailors AS S, Reserves AS R Where R.sid = S.sid and R.bid = 100 and S.rating &gt; 5 and R.day = &#39;8/9/09&#39;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.05540s from github-fe138-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-1dca3eab4ab3b2a00235feebb2fc218f0e91bbe06e140fb6ca67049215c66508.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-1f331009569afef1b6732009f2b35f38330c0837b8cf35ff15698f631aa4256d.js" type="text/javascript"></script>
      
      
  </body>
</html>

