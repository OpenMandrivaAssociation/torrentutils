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
