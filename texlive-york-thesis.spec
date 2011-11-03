# revision 23348
# category Package
# catalog-ctan /macros/latex/contrib/york-thesis
# catalog-date 2011-06-14 00:09:45 +0200
# catalog-license lppl1.3
# catalog-version 3.6
Name:		texlive-york-thesis
Version:	3.6
Release:	1
Summary:	A thesis class file for York University, Toronto
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/york-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
York Graduate Studies has again changed the requirements for
theses and dissertations. The established york-thesis class
file now implements the changes made in Spring 2005.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
