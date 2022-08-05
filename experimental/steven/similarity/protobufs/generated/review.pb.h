// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: review.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_review_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_review_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3021000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3021004 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_review_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_review_2eproto {
  static const uint32_t offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_review_2eproto;
namespace reviewers {
class Review;
struct ReviewDefaultTypeInternal;
extern ReviewDefaultTypeInternal _Review_default_instance_;
}  // namespace reviewers
PROTOBUF_NAMESPACE_OPEN
template<> ::reviewers::Review* Arena::CreateMaybeMessage<::reviewers::Review>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace reviewers {

// ===================================================================

class Review final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:reviewers.Review) */ {
 public:
  inline Review() : Review(nullptr) {}
  ~Review() override;
  explicit PROTOBUF_CONSTEXPR Review(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  Review(const Review& from);
  Review(Review&& from) noexcept
    : Review() {
    *this = ::std::move(from);
  }

  inline Review& operator=(const Review& from) {
    CopyFrom(from);
    return *this;
  }
  inline Review& operator=(Review&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  inline const ::PROTOBUF_NAMESPACE_ID::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance);
  }
  inline ::PROTOBUF_NAMESPACE_ID::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const Review& default_instance() {
    return *internal_default_instance();
  }
  static inline const Review* internal_default_instance() {
    return reinterpret_cast<const Review*>(
               &_Review_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(Review& a, Review& b) {
    a.Swap(&b);
  }
  inline void Swap(Review* other) {
    if (other == this) return;
  #ifdef PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() != nullptr &&
        GetOwningArena() == other->GetOwningArena()) {
   #else  // PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() == other->GetOwningArena()) {
  #endif  // !PROTOBUF_FORCE_COPY_IN_SWAP
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Review* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  Review* New(::PROTOBUF_NAMESPACE_ID::Arena* arena = nullptr) const final {
    return CreateMaybeMessage<Review>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const Review& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom( const Review& from) {
    Review::MergeImpl(*this, from);
  }
  private:
  static void MergeImpl(::PROTOBUF_NAMESPACE_ID::Message& to_msg, const ::PROTOBUF_NAMESPACE_ID::Message& from_msg);
  public:
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  uint8_t* _InternalSerialize(
      uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _impl_._cached_size_.Get(); }

  private:
  void SharedCtor(::PROTOBUF_NAMESPACE_ID::Arena* arena, bool is_message_owned);
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Review* other);

  private:
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "reviewers.Review";
  }
  protected:
  explicit Review(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kVersionFieldNumber = 1,
    kAuthorFieldNumber = 2,
    kMovieFieldNumber = 3,
    kRatingFieldNumber = 4,
  };
  // optional string version = 1;
  bool has_version() const;
  private:
  bool _internal_has_version() const;
  public:
  void clear_version();
  const std::string& version() const;
  template <typename ArgT0 = const std::string&, typename... ArgT>
  void set_version(ArgT0&& arg0, ArgT... args);
  std::string* mutable_version();
  PROTOBUF_NODISCARD std::string* release_version();
  void set_allocated_version(std::string* version);
  private:
  const std::string& _internal_version() const;
  inline PROTOBUF_ALWAYS_INLINE void _internal_set_version(const std::string& value);
  std::string* _internal_mutable_version();
  public:

  // optional string author = 2;
  bool has_author() const;
  private:
  bool _internal_has_author() const;
  public:
  void clear_author();
  const std::string& author() const;
  template <typename ArgT0 = const std::string&, typename... ArgT>
  void set_author(ArgT0&& arg0, ArgT... args);
  std::string* mutable_author();
  PROTOBUF_NODISCARD std::string* release_author();
  void set_allocated_author(std::string* author);
  private:
  const std::string& _internal_author() const;
  inline PROTOBUF_ALWAYS_INLINE void _internal_set_author(const std::string& value);
  std::string* _internal_mutable_author();
  public:

  // optional string movie = 3;
  bool has_movie() const;
  private:
  bool _internal_has_movie() const;
  public:
  void clear_movie();
  const std::string& movie() const;
  template <typename ArgT0 = const std::string&, typename... ArgT>
  void set_movie(ArgT0&& arg0, ArgT... args);
  std::string* mutable_movie();
  PROTOBUF_NODISCARD std::string* release_movie();
  void set_allocated_movie(std::string* movie);
  private:
  const std::string& _internal_movie() const;
  inline PROTOBUF_ALWAYS_INLINE void _internal_set_movie(const std::string& value);
  std::string* _internal_mutable_movie();
  public:

  // optional float rating = 4;
  bool has_rating() const;
  private:
  bool _internal_has_rating() const;
  public:
  void clear_rating();
  float rating() const;
  void set_rating(float value);
  private:
  float _internal_rating() const;
  void _internal_set_rating(float value);
  public:

  // @@protoc_insertion_point(class_scope:reviewers.Review)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  struct Impl_ {
    ::PROTOBUF_NAMESPACE_ID::internal::HasBits<1> _has_bits_;
    mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
    ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr version_;
    ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr author_;
    ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr movie_;
    float rating_;
  };
  union { Impl_ _impl_; };
  friend struct ::TableStruct_review_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// Review

// optional string version = 1;
inline bool Review::_internal_has_version() const {
  bool value = (_impl_._has_bits_[0] & 0x00000001u) != 0;
  return value;
}
inline bool Review::has_version() const {
  return _internal_has_version();
}
inline void Review::clear_version() {
  _impl_.version_.ClearToEmpty();
  _impl_._has_bits_[0] &= ~0x00000001u;
}
inline const std::string& Review::version() const {
  // @@protoc_insertion_point(field_get:reviewers.Review.version)
  return _internal_version();
}
template <typename ArgT0, typename... ArgT>
inline PROTOBUF_ALWAYS_INLINE
void Review::set_version(ArgT0&& arg0, ArgT... args) {
 _impl_._has_bits_[0] |= 0x00000001u;
 _impl_.version_.Set(static_cast<ArgT0 &&>(arg0), args..., GetArenaForAllocation());
  // @@protoc_insertion_point(field_set:reviewers.Review.version)
}
inline std::string* Review::mutable_version() {
  std::string* _s = _internal_mutable_version();
  // @@protoc_insertion_point(field_mutable:reviewers.Review.version)
  return _s;
}
inline const std::string& Review::_internal_version() const {
  return _impl_.version_.Get();
}
inline void Review::_internal_set_version(const std::string& value) {
  _impl_._has_bits_[0] |= 0x00000001u;
  _impl_.version_.Set(value, GetArenaForAllocation());
}
inline std::string* Review::_internal_mutable_version() {
  _impl_._has_bits_[0] |= 0x00000001u;
  return _impl_.version_.Mutable(GetArenaForAllocation());
}
inline std::string* Review::release_version() {
  // @@protoc_insertion_point(field_release:reviewers.Review.version)
  if (!_internal_has_version()) {
    return nullptr;
  }
  _impl_._has_bits_[0] &= ~0x00000001u;
  auto* p = _impl_.version_.Release();
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  _impl_.version_.Set("", GetArenaForAllocation());
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  return p;
}
inline void Review::set_allocated_version(std::string* version) {
  if (version != nullptr) {
    _impl_._has_bits_[0] |= 0x00000001u;
  } else {
    _impl_._has_bits_[0] &= ~0x00000001u;
  }
  _impl_.version_.SetAllocated(version, GetArenaForAllocation());
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  if (_impl_.version_.IsDefault()) {
    _impl_.version_.Set("", GetArenaForAllocation());
  }
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  // @@protoc_insertion_point(field_set_allocated:reviewers.Review.version)
}

// optional string author = 2;
inline bool Review::_internal_has_author() const {
  bool value = (_impl_._has_bits_[0] & 0x00000002u) != 0;
  return value;
}
inline bool Review::has_author() const {
  return _internal_has_author();
}
inline void Review::clear_author() {
  _impl_.author_.ClearToEmpty();
  _impl_._has_bits_[0] &= ~0x00000002u;
}
inline const std::string& Review::author() const {
  // @@protoc_insertion_point(field_get:reviewers.Review.author)
  return _internal_author();
}
template <typename ArgT0, typename... ArgT>
inline PROTOBUF_ALWAYS_INLINE
void Review::set_author(ArgT0&& arg0, ArgT... args) {
 _impl_._has_bits_[0] |= 0x00000002u;
 _impl_.author_.Set(static_cast<ArgT0 &&>(arg0), args..., GetArenaForAllocation());
  // @@protoc_insertion_point(field_set:reviewers.Review.author)
}
inline std::string* Review::mutable_author() {
  std::string* _s = _internal_mutable_author();
  // @@protoc_insertion_point(field_mutable:reviewers.Review.author)
  return _s;
}
inline const std::string& Review::_internal_author() const {
  return _impl_.author_.Get();
}
inline void Review::_internal_set_author(const std::string& value) {
  _impl_._has_bits_[0] |= 0x00000002u;
  _impl_.author_.Set(value, GetArenaForAllocation());
}
inline std::string* Review::_internal_mutable_author() {
  _impl_._has_bits_[0] |= 0x00000002u;
  return _impl_.author_.Mutable(GetArenaForAllocation());
}
inline std::string* Review::release_author() {
  // @@protoc_insertion_point(field_release:reviewers.Review.author)
  if (!_internal_has_author()) {
    return nullptr;
  }
  _impl_._has_bits_[0] &= ~0x00000002u;
  auto* p = _impl_.author_.Release();
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  _impl_.author_.Set("", GetArenaForAllocation());
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  return p;
}
inline void Review::set_allocated_author(std::string* author) {
  if (author != nullptr) {
    _impl_._has_bits_[0] |= 0x00000002u;
  } else {
    _impl_._has_bits_[0] &= ~0x00000002u;
  }
  _impl_.author_.SetAllocated(author, GetArenaForAllocation());
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  if (_impl_.author_.IsDefault()) {
    _impl_.author_.Set("", GetArenaForAllocation());
  }
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  // @@protoc_insertion_point(field_set_allocated:reviewers.Review.author)
}

// optional string movie = 3;
inline bool Review::_internal_has_movie() const {
  bool value = (_impl_._has_bits_[0] & 0x00000004u) != 0;
  return value;
}
inline bool Review::has_movie() const {
  return _internal_has_movie();
}
inline void Review::clear_movie() {
  _impl_.movie_.ClearToEmpty();
  _impl_._has_bits_[0] &= ~0x00000004u;
}
inline const std::string& Review::movie() const {
  // @@protoc_insertion_point(field_get:reviewers.Review.movie)
  return _internal_movie();
}
template <typename ArgT0, typename... ArgT>
inline PROTOBUF_ALWAYS_INLINE
void Review::set_movie(ArgT0&& arg0, ArgT... args) {
 _impl_._has_bits_[0] |= 0x00000004u;
 _impl_.movie_.Set(static_cast<ArgT0 &&>(arg0), args..., GetArenaForAllocation());
  // @@protoc_insertion_point(field_set:reviewers.Review.movie)
}
inline std::string* Review::mutable_movie() {
  std::string* _s = _internal_mutable_movie();
  // @@protoc_insertion_point(field_mutable:reviewers.Review.movie)
  return _s;
}
inline const std::string& Review::_internal_movie() const {
  return _impl_.movie_.Get();
}
inline void Review::_internal_set_movie(const std::string& value) {
  _impl_._has_bits_[0] |= 0x00000004u;
  _impl_.movie_.Set(value, GetArenaForAllocation());
}
inline std::string* Review::_internal_mutable_movie() {
  _impl_._has_bits_[0] |= 0x00000004u;
  return _impl_.movie_.Mutable(GetArenaForAllocation());
}
inline std::string* Review::release_movie() {
  // @@protoc_insertion_point(field_release:reviewers.Review.movie)
  if (!_internal_has_movie()) {
    return nullptr;
  }
  _impl_._has_bits_[0] &= ~0x00000004u;
  auto* p = _impl_.movie_.Release();
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  _impl_.movie_.Set("", GetArenaForAllocation());
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  return p;
}
inline void Review::set_allocated_movie(std::string* movie) {
  if (movie != nullptr) {
    _impl_._has_bits_[0] |= 0x00000004u;
  } else {
    _impl_._has_bits_[0] &= ~0x00000004u;
  }
  _impl_.movie_.SetAllocated(movie, GetArenaForAllocation());
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  if (_impl_.movie_.IsDefault()) {
    _impl_.movie_.Set("", GetArenaForAllocation());
  }
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  // @@protoc_insertion_point(field_set_allocated:reviewers.Review.movie)
}

// optional float rating = 4;
inline bool Review::_internal_has_rating() const {
  bool value = (_impl_._has_bits_[0] & 0x00000008u) != 0;
  return value;
}
inline bool Review::has_rating() const {
  return _internal_has_rating();
}
inline void Review::clear_rating() {
  _impl_.rating_ = 0;
  _impl_._has_bits_[0] &= ~0x00000008u;
}
inline float Review::_internal_rating() const {
  return _impl_.rating_;
}
inline float Review::rating() const {
  // @@protoc_insertion_point(field_get:reviewers.Review.rating)
  return _internal_rating();
}
inline void Review::_internal_set_rating(float value) {
  _impl_._has_bits_[0] |= 0x00000008u;
  _impl_.rating_ = value;
}
inline void Review::set_rating(float value) {
  _internal_set_rating(value);
  // @@protoc_insertion_point(field_set:reviewers.Review.rating)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace reviewers

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_review_2eproto
