%define name torrentutils
%define version 0.3.0
%define release %mkrel 10

Summary: Utilities for BitTorrent files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://oskarsapps.mine.nu/src/%{name}-%{version}.tar.bz2
URL: http://oskarsapps.mine.nu/torrentutils.html
License: GPL or Artistic
Group: Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: perl

%description
The torrentutils are a set of utilities for managing BitTorrent
(`.torrent') files and interactiving with BitTorrent trackers. The
torrentutils contain the following programs:

torrenttool is a script that extracts and displays information from
BitTorrent files, as well as testing and generating checksums for
files listed in them.

defrag is a script that defrags files simply by making a copy of the
file. The original file is then replaced by the copy. Due to the fact
that BitTorrent splits files in pieces, and downloads these pieces in
random order, the downloaded files are often severely fragmented. This
means that reading these files will be slower, sometimes as much as
30% slower. defrag can also recurse directories.

torrentmcfs is a read-only virtual file system for Midnight Commander
that can be used to easier access the information in a BitTorrent
file.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=%buildroot%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README COPYING*
%_bindir/torrenttool
%_bindir/defrag
%_mandir/man1/torrenttool.1*
%_mandir/man1/defrag.1*
%_datadir/mc/extfs/torrentmcfs


%changelog
* Fri Aug 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-10mdv2012.0
+ Revision: 693277
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-9mdv2011.0
+ Revision: 261626
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-8mdv2009.0
+ Revision: 254691
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 0.3.0-6mdv2008.1
+ Revision: 187629
- rebuild for 2008.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-5mdv2008.0
+ Revision: 57475
- Import torrentutils



* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-1mdv2007.0
- Rebuild

* Wed Mar  1 2006 Götz Waschk <waschk@mandriva.org> 0.3.0-4mdk
- new URL

* Tue Nov 08 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-3mdk
- Rebuild

* Fri Nov  5 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-2mdk
- rebuild

* Sun Oct 12 2003 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- add the torrentmcfs
- update description
- new version

* Wed Oct  8 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-1mdk
- add %%_bindir/defrag
- update description
- new version

* Mon Aug 18 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.0-1mdk
- initial package
