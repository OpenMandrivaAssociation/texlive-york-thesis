Name:		texlive-york-thesis
Version:	23348
Release:	1
Summary:	A thesis class file for York University, Toronto
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/york-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
York Graduate Studies has again changed the requirements for
theses and dissertations. The established york-thesis class
file now implements the changes made in Spring 2005.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/york-thesis/york-thesis.cls
%doc %{_texmfdistdir}/doc/latex/york-thesis/README
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis-Template.tex
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis.el
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/york-thesis/york-thesis.dtx
%doc %{_texmfdistdir}/source/latex/york-thesis/york-thesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
