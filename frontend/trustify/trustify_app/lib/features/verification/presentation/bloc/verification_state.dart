part of 'verification_bloc.dart';

@immutable
sealed class VerificationState {}

final class VerificationInitial extends VerificationState {}

final class LinkVerified extends VerificationState {
  final Map<String, dynamic> data;
  LinkVerified(this.data);
}

final class VerificationFailure extends VerificationState {
  final String message;
  VerificationFailure(this.message);
}
