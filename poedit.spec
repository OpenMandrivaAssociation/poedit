Summary:	Gettext translation file editor
Name:		poedit
Version:	1.5.2
Release:	1
License:	MIT
Group:		Editors
URL:		http://www.poedit.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:	gettext
BuildRequires:	wxgtku-devel >= 2.8
BuildRequires:	db-devel
BuildRequires:	gtkspell-devel
BuildRequires:	zip
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
Requires(Pre):	shared-mime-info
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Poedit is cross-platform gettext catalogs (.po files) editor. It is built with
wxWindows toolkit and can run on Unix or Windows. It aims to provide convenient
way of editing gettext catalogs. It features UTF-8 support, fuzzy and
untranslated records highlighting, whitespaces highlighting, references
browser, headers editing and can be used to create new catalogs or update
existing catalogs from source code by single click.

%prep
%setup -q

%build
# wx-config is brain-damaged. Damn you, multiarch, damn you
%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
%make

%install
%makeinstall_std

desktop-file-install \
  --add-category="GTK;GNOME;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove files not bundled
rm -f %{buildroot}/%{_iconsdir}/poedit.xpm

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS TODO 
%dir %{_datadir}/poedit
%{_bindir}/poedit
%{_iconsdir}/*
%{_mandir}/man1/*
%{_datadir}/poedit/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*


%changelog
* Sat Aug 11 2012 Johnny A. Solbu <solbu@mandriva.org> 1.5.2-1
+ Revision: 814025
- Fix BuildRequires
- New version
- Spec cleanup

* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 1.4.6.1-4
+ Revision: 797441
- Rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - rebuild against db 5.1.25

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.6.1-2mdv2011.0
+ Revision: 614602
- the mass rebuild of 2010.1 packages

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean spec

* Wed Apr 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.6.1-1mdv2010.1
+ Revision: 532633
- update to 1.4.6.1

* Tue Feb 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.5-1mdv2010.1
+ Revision: 499747
- New release 1.4.5

* Sat Jan 30 2010 Frederik Himpe <fhimpe@mandriva.org> 1.4.4-1mdv2010.1
+ Revision: 498508
- Revert db4.8-devel BuildRequires, db-devel is OK
- BuildRequires desktop-file-utils
- Update to new version 1.4.4
- Use desktop-file-install in spec file instead of patch to fix
  desktop file

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix BuildRequires db-devel to db4.8-devel

* Wed Dec 30 2009 Funda Wang <fwang@mandriva.org> 1.4.3-2mdv2010.1
+ Revision: 484099
- rebuild for db4.8

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.3-1mdv2010.0
+ Revision: 444890
- update to new version 1.4.3

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.2-5mdv2010.0
+ Revision: 441884
- rebuild

* Tue Feb 24 2009 Emmanuel Andry <eandry@mandriva.org> 1.4.2-4mdv2009.1
+ Revision: 344535
- switch to db4.7

* Tue Feb 24 2009 Emmanuel Andry <eandry@mandriva.org> 1.4.2-3mdv2009.1
+ Revision: 344421
- rebuild

* Wed Oct 01 2008 Funda Wang <fwang@mandriva.org> 1.4.2-2mdv2009.0
+ Revision: 290309
- fix wrong locale location

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 1.4.2-1mdv2009.0
+ Revision: 282073
- update to new version 1.4.2

* Sat Jun 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-2mdv2009.0
+ Revision: 229885
- do not package COPYING file

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 04 2008 Frederik Himpe <fhimpe@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 200924
- New version

* Sun Jan 13 2008 Emmanuel Andry <eandry@mandriva.org> 1.3.9-2mdv2008.1
+ Revision: 150435
- use db4.6

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - fix name and URL

* Tue Dec 11 2007 Funda Wang <fwang@mandriva.org> 1.3.9-1mdv2008.1
+ Revision: 117337
- New version 1.3.9

* Tue Jul 10 2007 Funda Wang <fwang@mandriva.org> 1.3.7-1mdv2008.0
+ Revision: 50799
- BR wxgtku 2.8
- BR gtk2.6-devel
- New version


* Sun Mar 04 2007 Emmanuel Andry <eandry@mandriva.org> 1.3.6-3mdv2007.0
+ Revision: 131942
- build with wxgtk2.8 and db4.5

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 1.3.6-2mdv2007.1
+ Revision: 100704
- rebuild

* Sun Dec 03 2006 Emmanuel Andry <eandry@mandriva.org> 1.3.6-1mdv2007.1
+ Revision: 90147
- New version 1.3.6
- Drop patch0
  xdg menu

  + Lenny Cartier <lenny@mandriva.com>
    - Import poedit

* Sat Nov 26 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.3.4-2mdk
- rebuild against libcairo2
- macroszification

* Wed Oct 05 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.3.4-1mdk
- 1.3.4

* Wed Jul 06 2005 Abel Cheung <deaddog@mandriva.org> 1.3.3-2mdk
- Make sure to build with wxGTK 2.6 with unicode support
- makeinstall_std
- Drop semistatic support, never tested and broken for ages
- Use source bundled icons, which are much clearer
- Patch0: Avoid detection of GNOME/KDE desktop. Install desktop
  stuff manually to avoid annoying GNOME 1.x / KDE dependency

* Tue Jun 28 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.3.3-1mdk
- 1.3.3
- use mkrel

* Sat Jan 29 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.2-1mdk
- 1.3.2

* Thu Sep 16 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.1-1mdk
- 1.3.1
- removed P0
- makeinstall instead of makeinstall_std
- build with gtkspell
- fixed menu section

* Wed Sep 08 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.0-1mdk
- 1.3.0
- this version is a little bit broken, there is some known nasty bugs which
  will be fixed in 1.3.1 available soon
- added temporary P0 which allow build poedit with wxGTK2.5.1 (thanks for patch
  to Vaclav Slavik)
- improved icons installation

* Tue Jun 08 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.2.5-2mdk
- rebuild with libstdc++6
- some macroszification, update section

